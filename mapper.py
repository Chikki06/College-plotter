import http.client, urllib.parse
import json
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import pandas as pd
file = open(r"C:\Users\hiidk\Projects\text scraping\info.txt","r+")
lines = []
lines = file.readlines()
count = 0
latlong = {}
latlong["Names"] = []
latlong["Latitude"] = []
latlong["Longitude"] = []
for x in range(1,122,3):
    name = lines[x]

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': '7768124fc935c2275a68100f90229746',
        'query': f'{name}',
        'region': f'{name}',
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
# df = pd.DataFrame(list(latlong.items()),columns = ['Name','Latitude','Longitude'])
# print(df.head())
