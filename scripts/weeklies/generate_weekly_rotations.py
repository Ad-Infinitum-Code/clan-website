import json
import pathlib
from dataclasses import dataclass
from itertools import cycle
from typing import Tuple

import pandas
import yaml


CWD = pathlib.Path(__file__).parent.resolve()
WEEKLIES_YAML_PATH = CWD / "../../extra-yaml/weeklies.yml"
ROTATION_YAML_PATH = CWD / "rotation.yml"
JSON_FILE_PATH = CWD / "rotation.json"
CURRENT_SEASON = 18


@dataclass
class Rotation:
    """Class for holding rotation information"""

    date: str
    vanguard: str
    nightfall: str
    adept: str
    dungeon: str
    raid: str


def convert_timestamp_to_date_string(timestamp: pandas.Timestamp) -> str:
    """Given a pandas.Timestamp object, return a date string in the format YYYY-MM-DD"""

    return timestamp.strftime("%Y-%m-%d")


def write_dict_to_json_file(data: dict, filepath):
    """Write a given dictionary to a .json file

    Positional args:

        data - dictionary of data to dump into a .json file

        filepath - absolute path for output .json file
    """

    with open(filepath, "w") as f:
        json.dump(data, f)


def load_json_from_file(filepath) -> dict:
    """Load a .json file from disk and return it as a dict

    Positional args:

        filepath - absolute path for input .json file
    """

    with open(filepath, "r") as f:
        data = f.read()

    return data


def create_rotation_list(
    rotation: dict, dates: pandas.DatetimeIndex
) -> Tuple[list, Rotation]:
    """Populate the rotations for given set of dates

    Positional args:

        rotation - dict created from loading rotation.yml

        dates - DatetimeIndex of all Tuesdays (weekly reset) during the season

    Return: list of Rotation objects populated with given data
    """

    # The list of dates will always be longer than any of the rotation lists.
    # Therefore, we use itertools.cycle to "wrap around" the shorter lists and repeat pattern while we iterate through all the dates.
    # This ends up as a list of tuples: [[pandas.DatetimeIndex, vanguard, nightfall, adept, dungeon, raid], ...]
    zipped = list(
        zip(
            dates,
            cycle(rotation[CURRENT_SEASON]["vanguard"]),
            cycle(rotation[CURRENT_SEASON]["nightfall"]),
            cycle(rotation[CURRENT_SEASON]["adept"]),
            cycle(rotation[CURRENT_SEASON]["dungeon"]),
            cycle(rotation[CURRENT_SEASON]["raid"]),
        )
    )

    # The return list holding all created Rotation objects
    ret = []

    # Figure out what the current week is so we can return the current rotation
    current_week = determine_current_week(dates)
    current_rotation = None

    # Create rotation objects for each tuple of data
    for i in zipped:
        rotation_date = convert_timestamp_to_date_string(i[0])

        x = Rotation(
            rotation_date,
            vanguard=i[1],
            nightfall=i[2],
            adept=i[3],
            dungeon=i[4],
            raid=i[5],
        )

        ret.append(x)

        # If same, now we have the current rotation
        if rotation_date == current_week:
            current_rotation = x

    return ret, current_rotation


def determine_current_week(dates: pandas.DatetimeIndex) -> str:
    """Given a pandas.DatetimeIndex object, return a YYYY-MM-DD date string matching the below criteria.

    We want to find which week we are in by using a list of dates as well as a current timestamp.
    Basically, the latest date where: previous_date <= current_date < future date

    Positional args:

        dates - a pandas.DatetimeIndex of dates

    Return: YYYY-MM-DD date string
    """

    now = pandas.Timestamp.now()

    week_idx = 0
    for i in dates:
        if i < now:
            week_idx += 1
        else:
            break

    # Have to subtract 1, since the first index (0) date will always be less than the current timestamp
    # The timestamps are all at 00:00:00, our now timestamp will never be at 00:00:00 since it'll run at at weekly reset time
    week_idx -= 1

    return convert_timestamp_to_date_string(dates[week_idx])


def create_weeklies_yaml(rotation: Rotation):
    """Given a Rotation object, save a .yml file with the below format/information"""

    # Create the dict with our information
    yaml_dict = {
        "extra": {
            "weekly": {
                "date": rotation.date,
                "vanguard": rotation.vanguard,
                "nightfall": rotation.nightfall,
                "adept": rotation.adept,
                "dungeon": rotation.dungeon,
                "raid": rotation.raid,
            }
        }
    }

    # Write it to the file
    with open(WEEKLIES_YAML_PATH, "w") as f:
        yaml.dump(yaml_dict, f)


if __name__ == "__main__":

    # Pull in the current rotation information via rotation.yml
    with open(ROTATION_YAML_PATH, "r") as f:
        rotation = yaml.load(f, Loader=yaml.FullLoader)

    # Find the season start/end dates
    start_date = rotation[CURRENT_SEASON]["start"]
    end_date = rotation[CURRENT_SEASON]["end"]

    # Create a pandas.DatetimeIndex for all Tuesdays within the start/end dates
    dates = pandas.date_range(start_date, end_date, freq="W-TUE")[:-1]

    # Create our rotations
    rotation_list, current_rotation = create_rotation_list(rotation, dates)

    print("Current rotation:")
    print(current_rotation)

    # Save/update the rotation.yml for use in docs/weeklies/index.md
    create_weeklies_yaml(current_rotation)
