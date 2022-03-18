import http.client, urllib.parse
import json
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import pandas as pd
file = open(r"<path here>","r+")
lines = []
lines = file.readlines()
latlong = {}
latlong["Names"] = []
latlong["Latitude"] = []
latlong["Longitude"] = []
for x in range(1,122,3):
    name = lines[x]

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': '<Key here>',
        'query': f'{name}',
        'region': f'{name}, North America',
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    fin = json.loads(data)
    latlong["Names"].append(f'{name[:-1]}')
    latlong["Latitude"].append(fin['data'][0]['latitude'])
    latlong["Longitude"].append(fin['data'][0]['longitude'])
print(latlong)
df = pd.DataFrame(latlong)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
print(gdf)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
map = world[world.continent == 'North America'].plot(color='lightblue', edgecolor='black')
gdf.plot(ax = map, color='red')

plt.show()
