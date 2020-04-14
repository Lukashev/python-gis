import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

fp = "addresses.shp"

data = gpd.read_file(fp)

# Let's take a copy of our layer
data_proj = data.copy()
# Reproject the geometries by replacing the values with projected ones
data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=3879)

# print(data_proj.crs)

# print(data_proj['geometry'].head())


data.plot(markersize=6, color="red");

plt.title("WGS84 projection");

plt.tight_layout()

data_proj.plot(markersize=6, color="blue");

plt.title("ETRS GK-25 projection");

plt.tight_layout()
plt.show()

# data_proj.crs = from_epsg(3879)
#
# data_proj.crs = {'y_0': 0, 'no_defs': True, 'x_0': 25500000, 'k': 1, 'lat_0': 0,
# 'units': 'm', 'lon_0': 25, 'ellps': 'GRS80', 'proj': 'tmerc'}
#
# print(data_proj.crs)
#
# outfp = r"addresses_epsg3879.shp"
#
# data_proj.to_file(outfp)
