"""
Loads data from txt files
"""

## TODO:
## * build a scraper to load data dynamically



file = "starwars.txt"

with open(file, 'r') as f:
    data = f.read()