import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2700

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = [
    # "eby",
    "sfc",
    # "sby",
    # "nby",
]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "north beach": [
        (37.79820, -122.41222),
        (37.80602, -122.40342)
    ],
    "western addition": [
        (37.77354, -122.43850),
        (37.78390, -122.42258)
    ],
    "lower haight": [
        (37.77022, -122.43926),
        (37.77364, -122.42737)
    ],
    "potrero hill": [
        (37.74939, -122.40466),
        (37.76620, -122.39282)
    ],
    "noe valley": [
        (37.74148, -122.44477),
        (37.75663, -122.42418),
    ],
    "bernal heights": [
        (37.73827, -122.42301),
        (37.74777, -122.40902)
    ],
    "lower pac heights": [
        (37.78554, -122.42878),
        (37.78873, -122.44544),
    ],
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = [
    "north beach",
    "western addition",
    "lower haight",
    "cow hollow",
    "pac hts",
    "pacific heights",
    "noe valley",
    "bernal heights",
    "potrero hill",
    "hayes valley",
    "nob hill",
]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 20 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051, -122.2720873],
    "macarthur_bart": [37.8265657, -122.2686705],
    "rockridge_bart": [37.841286, -122.2566329],
    "downtown_berkeley_bart": [37.8629541, -122.276594],
    "north_berkeley_bart": [37.8713411, -122.2849758],
    "16th_street_mission_bart": [37.765057, -122.419702],
    "24th_street_mission_bart": [37.752467, -122.418156],
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass