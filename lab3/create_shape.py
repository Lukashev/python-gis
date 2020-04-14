import pandas as pd
from geopandas.tools import geocode

fp = r"shopping_centers.txt"

data = pd.read_csv(fp, sep=';')

geo = geocode(data['address'], provider='arcgis')

df = geo.join(data, lsuffix='_left', rsuffix='_right')

outfp = r"addresses.shp"

df.to_file(outfp)




