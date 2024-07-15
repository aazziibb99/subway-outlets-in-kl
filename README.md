# subway-outlets-in-kl

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## About


## Features


## Installation
'''bash
# create virtual environment
python -m venv venv

# activate virtual environment
venv\scripts\activate

# install packages
pip install -r requirements.txt

# get data by scraping subway find-a-store website
python scraper.py

# get geocode for each outlet based on address
python geocode.py
'''

## Usage
'''bash
# rename .env.example file to .env
# open .env file and add your own google maps api key

# start the app
uvicorn main:app -reload

# open the url in the terminal
'''
