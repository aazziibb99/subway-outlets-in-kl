# subway-outlets-in-kl

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## About


## Features


## Installation

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

get data by scraping subway find-a-store website
```terminal
python scraper.py
```

get geocode for each outlet based on address
```terminal
python geocode.py
```

## Usage
```terminal
# rename .env.example file to .env
# open .env file and add your own google maps api key

# start the app
uvicorn main:app -reload

# open the url in the terminal
```
