# Project RedHorse

# Table of Contents
1. [What the?](#what-the)
1. [Quickstart](#quickstart)
1. [Pre-Commit](#pre-commit)
1. [Testing](#testing)
1. [Linting](#linting)
1. [File Formatter](#file-formatter)

## What the?
Okay, I'm tired of re-creating new Flask back-end over and over again when working on a project.

It's called RedHorse because the project is Flask... He he he.

## Quickstart
1. Fork the repo
1. Navigate to the project folder
1. Run `flask run`
1. Open your browser to `http://localhost:5000/apidocs`

## Pre-Commit
The project uses [Pre-Commit](https://pre-commit.com/) package to configure the pre-commit hook. Right now, it is configured to run [Flake8](#linting) along with [Black Formatter](#file-formatter).

The pre-commit is configured in `.pre-commit-config.yaml`.

Installing the pre-commit hook in your local machine:
1. Navigate to project folder
1. Run `pre-commit install`

## Testing
Unit testing is very very simple. The project uses [PyTest](https://docs.pytest.org/en/latest/) - a framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries (Lul copy pasta!)

To run the test, simply navigate to the project folder and run `pytest`

## Linting
Lint configuration is based-off of [Flake8](https://pypi.org/project/flake8/) with few configuration.
See `.flake8` file.

Running Flake8:
1. Navigate to project folder
1. Run `flake8 <file_regex>

## File Formatter
The project uses [Black](https://github.com/psf/black) to format the Python scripts

Running the formatter:
1. Navigate to project folder
1. Run `black <file_regex>`
