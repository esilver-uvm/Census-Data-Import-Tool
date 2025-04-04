# United States of America Python Dictionary to translate States,
# Districts & Territories to Two-Letter codes and vice versa.
#
# Canonical URL: https://gist.github.com/rogerallen/1583593
#
# Dedicated to the public domain.  To the extent possible under law,
# Roger Allen has waived all copyright and related or neighboring
# rights to this code.  Data originally from Wikipedia at the url:
# https://en.wikipedia.org/wiki/ISO_3166-2:US
#
# Automatically Generated 2024-10-08 07:45:06 via Jupyter Notebook from
# https://gist.github.com/rogerallen/d75440e8e5ea4762374dfd5c1ddf84e0

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "Virgin Islands, U.S.": "VI",
}

cols_labels = ["Tract Code",
               "State",
               "County",
               "Latitude",
               "Longitude",
               "Total Cash Rent",
               "Total Cash Rent MG",
               'Less than $100',
               'Less than $100 MG',
               '$100 to $149',
               '$100 to $149 MG',
               '$150 to $199',
               '$150 to $199 MG',
               '$200 to $249',
               '$200 to $249 MG',
               '$250 to $299',
               '$250 to $299 MG',
               '$300 to $349',
               '$300 to $349 MG',
               '$350 to $399',
               '$350 to $399 MG',
               '$400 to $449',
               '$400 to $449 MG',
               '$450 to $499',
               '$450 to $499 MG',
               '$500 to $549',
               '$500 to $549 MG',
               '$550 to $599',
               '$550 to $599 MG',
               '$600 to $649',
               '$600 to $649 MG',
               '$650 to $699',
               '$650 to $699 MG',
               '$700 to $749',
               '$700 to $749 MG',
               '$750 to $799',
               '$750 to $799 MG',
               '$800 to $899',
               '$800 to $899 MG',
               '$900 to $999',
               '$900 to $999 MG',
               '$1,000 to $1,249',
               '$1,000 to $1,249 MG',
               '$1,250 to $1,499',
               '$1,250 to $1,499 MG',
               '$1,500 to $1,999',
               '$1,500 to $1,999 MG',
               '$2,000 to $2,499',
               '$2,000 to $2,499 MG',
               '$2,500 to $2,999',
               '$2,500 to $2,999 MG',
               '$3,000 to $3,499',
               '$3,000 to $3,499 MG',
               '$3,500 or more',
               '$3,500 or more MG',
               'No Cash Rent',
               'No Cash Rent MG']
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))


