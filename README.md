# subway-outlets-in-kl

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries](#libraries)

## about
collecting data on subway kuala lumpur outlets such as branch name, address, waze link using web scraping tools and getting geographical coordinate of each store using third party api. the data then be served on a spa to show the location of selected outlet and other surrounding landmarks within 5km radius.

## features
- automated web scraping process using selenium
- get geocode using google maps geocoder api
- simple api to serve interface containing the collected data using fastapi
- highlight catchment in 5km radius of selected store

## installation

create virtual environment
```terminal
python -m venv venv
```

activate virtual environment
```terminal
venv\scripts\activate
```

install packages
```terminal
pip install -r requirements.txt
```

## usage
!!! important !!!
- make sure internet connection is available

to-do first:
- rename .env.example file to .env
- open .env file and add personal google maps api key
- (optional) delete database.db file if running web scraper and geocoder

(optional if database.db deleted) to get data by scraping subway find-a-store website
```terminal
python scraper.py
```

(optional if database.db deleted) get geocode for each outlet based on address
```terminal
python geocode.py
```

run server and open the url to view the interface
```terminal
uvicorn main:app -reload
```

## libraries
backend
- selenium
- peewee
- requests
- fastapi
- uvicorn

frontend
- tailwind css
- daisyui
- alpine js
- axios

apis
- google maps
- google maps geocoder
