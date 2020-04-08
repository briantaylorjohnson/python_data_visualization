# Mapping Global Data Sets: JSON Format

# Import the Python JSON module
import json

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'

# Opens the file and extracts all data within
with open(filename) as f:
    all_eq_data = json.load(f)

# Extracts all earthquake dictionaries in the data source
all_eq_dicts = all_eq_data['features']

# Extracts all earthquake magnitudes from each earthquake dictionary
mags = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

# Extracts all location data from each earthquake dictionary
lons, lats = [], []

for eq_dict in all_eq_dicts:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)




