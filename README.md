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