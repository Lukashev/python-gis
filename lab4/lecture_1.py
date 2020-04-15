import geopandas as gpd
import matplotlib.pyplot as plt

# File paths

border_fp = 'data/Helsinki_borders.shp'
grid_fp = 'data/TravelTimes_to_5975375_RailwayStation.shp'

# Read files

grid = gpd.read_file(grid_fp)
hel = gpd.read_file(border_fp)

# print(hel.crs == grid.crs)

# basemap = hel.plot()

# grid.plot(ax=basemap, linewidth=0.02)

# Use tight layout
# plt.tight_layout()
# plt.show()

result = gpd.overlay(grid, hel, how='intersection')
# result.plot(color='b')

# Use tight layout
# plt.tight_layout()
# plt.show()

# print(result.head())
# print(len(result))
# print(len(grid))

# resultfp = 'data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson'

# Use GeoJSON driver
# result.to_file(resultfp, driver='GeoJSON')

result_aggregated = result.dissolve(by='car_r_t')

# What do we have now
# print(result_aggregated.head())

print(len(result))

print(len(result_aggregated))
