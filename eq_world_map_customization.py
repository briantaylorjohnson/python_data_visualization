# Mapping Global Data Sets: JSON Format

# Import the Python JSON module
import json

# Import Plotly modules for visualizations and offline output
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'

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

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags], # Sets the size of the earthquake marker relative to the magnitude (higher magnitude, bigger marker)
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

