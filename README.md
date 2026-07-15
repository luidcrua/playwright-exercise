# Test Automation challenge

## Description
This repo is intended for testing purposes. You are provided with a small Django web application (a login page and a dashboard) and a Playwright test suite that covers the login flow. The test suite works, but it was written in a hurry.

## Getting started

Copying the repository

Due to the public nature of forks we suggest you duplicate the repo rather than forking it.
You will need to create your own repo e.g. `[your_github_username]/test-automation-challenges` and then clone this repo and push the code into your new one. You can follow the steps for doing this here: https://help.github.com/articles/duplicating-a-repository/

Before proceeding be aware that this exercise assumes you are using a linux machine with [pip](https://pip.pypa.io/en/stable) and [venv](https://docs.python.org/3/library/venv.html) installed.

To initialize the repository in your base directory execute `./initialize_repo.sh`

This script will install Django 5.2 and other libraries required for the application, run the database migrations, and download the Chromium browser used by Playwright.

To start the application:

    ve/bin/python mysite/manage.py runserver

To run the test suite (with the application running):

    ve/bin/pytest

## The exercise

25-minute exercise.
Goal: Improve reliability and maintainability. AI/tools allowed.
Known issues exist in test code, not necessarily app.
Consider waits, locators, duplication, assertions, helpers/page objects, constants, fixtures.
Be ready to explain priorities.
