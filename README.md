# Test Automation challenge

## Description
This repo is intended for testing purposes. You are provided with a small Django web application (a login page and a dashboard) and a Playwright test suite that covers the login flow. The test suite works, but it was written in a hurry.

## Getting started

First of all, you need to clone this repository in your local machine.

Before proceeding be aware that this exercise assumes you are using a linux machine with [pip](https://pip.pypa.io/en/stable) and [venv](https://docs.python.org/3/library/venv.html) installed.

To initialize the repository in your base directory execute `./initialize_repo.sh`. This script will install Django 5.2 and other libraries required for the application, run the database migrations, and download the Chromium browser used by Playwright.

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
