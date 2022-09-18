<div align="center">
    <h1>
        <img src="docs/assets/images/infinity.svg" height=20>
        Ad Infinitum Clan Website
        <img src="docs/assets/images/infinity.svg" height=20>
    </h1>
    <img src="https://img.shields.io/github/repo-size/Ad-Infinitum-Code/clan-website">
    <img src="https://github.com/Ad-Infinitum-Code/clan-website/actions/workflows/ci.yml/badge.svg">
    <img src="https://img.shields.io/github/deployments/Ad-Infinitum-Code/clan-website/github-pages?label=gh-pages-env">
    <img src="https://img.shields.io/github/issues/Ad-Infinitum-Code/clan-website">
    <img src="https://img.shields.io/github/issues-pr/Ad-Infinitum-Code/clan-website">
    <hr>
</div>


## Overview

This repo is used to create/host the Ad Infinitum clan website, powered by [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and hosted via [Github Actions](https://github.com/features/actions).

Available here: https://ad-infinitum-code.github.io/clan-website/

## Repo Structure

Here's a basic rundown of how everything is laid out:

- `.github` - contains the workflow for building and publishing the site via Github Actions

- `docs` - contains all of the markdown files for the site, as well as other required assets (icons/images/styling/etc.)

- `overrides` - contains files used to override the base MkDocs Material things

- `mkdocs.yml` - contains all the config for MkDocs

## Docs Structure

The goal is to organize the files into subdirectories based on how they'll be displayed on the site.

For example, the `dungeons` folder corresponds to the `Dungeons` page on the site and contains named subfolders for each dungeon. Inside each individual dungeon folder will be the markdown file as well as any other assets for that dungeon (images mostly)

MkDocs will automatically generate the website based on the file structure, however in our case that's not desired because we'd like our raids and dungeons listed in chronological order. This is fixed by making an explicit navigation tree in [mkdocs.yml](https://github.com/Ad-Infinitum-Code/clan-website/blob/86471e680692164c66e4eba67f11598d84f9899d/mkdocs.yml#L52)

## Environment Setup

In order to make changes/additions, you'll need to get yourself a working environment. I'd highly recommend a Linux environment of your choosing as it's a lot simpler than dealing with Windows.

### Linux

1. Clone the repo:

    `git clone <repo URL>`

2. Ensure you have a recent version of Python3 installed:

    Debian/Ubuntu:
    
    `sudo apt update && sudo apt install python3 python3-venv -y`

3. Set up a virtual environment for the pip packages:

    From the root of the repo:
    
    `python3 -m venv venv`

    You'll now have a folder called `venv`

4. Activate the virtual environment:

    `source venv/bin/activate`

    You should see `(venv)` at the beginning of  your terminal line 

5. Install the pip requirements:

    `pip3 install -r requirements.txt`

6. Everything should now be set up for you!

### Windows

TBD


## Running MkDocs locally

As you're making changes, it's helpful to see them happen in realtime. 

### Linux

Assuming you have the environment set up and virtual environment activated, it should be as easy as:

1. Run the local version:

    `mkdocs serve`

2. Open your browser to version now being hosted by you locally:

    `http://127.0.0.1:8000/`

    or

    `http://localhost:8000/`

3. Make and save changes to something

4. See your changes update automagically

5. When you're done, stop it:

    `[Ctrl] + [C]`

If you want to see what the file structure looks like after building with mkdocs, run the following:

- `mkdocs build`

You'll now have a site folder containing all the generated static site files. This is essentially what the Github Actions does, generate everything and then host the `site` folder

### Windows

TBD


## Pushing your changes

Ideally, your changes should be on a different branch than master. Make your own branch, push your changes to it, and then open a pull request to have them merged in.

## Dependency management via pip-tools

Simply installing the required packages via `pip3 install -r requirements.txt` should be enough to develop locally.

However, `pip-tools` provides a nice interface for managing main/dev requirements.

### Setup

1. Create a virtual environment and activate it
    - `python3 -m venv venv`
    - `source venv/bin/activate`

2. Install pip-tools
    - `pip3 install pip-tools`

3. Install required main dependencies
    - `pip-sync`

4. You should be good to go

### Extras

To install the dev dependencies:

- `pip-sync requirements.txt dev-requirements.txt`

- Note: there's only pip-tools in there for now

To update main dependencies:

- `pip-compile requirements.in`

To update dev dependencies:

- update the main dependencies per above
- `pip-compile requirements-dev.in`