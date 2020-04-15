import geopandas as gpd
import numpy as np

# File paths
border_fp = "/home/geo/data/Helsinki_borders.shp"
grid_fp = "/home/geo/data/TravelTimes_to_5975375_RailwayStation.shp"
# Read files
grid = gpd.read_file(grid_fp)
hel = gpd.read_file(border_fp)
# Batch size
b = 10
# Number of iterations (round up with np.ceil) and convert to integer
row_cnt = len(grid)
iterations = int(np.ceil(row_cnt / b))
# Final result
final = gpd.GeoDataFrame()
# Set the start and end index according the batch size
start_idx = 0
end_idx = start_idx + b
for iteration in range(iterations):
    print("Iteration: %s/%s" % (iteration, iterations))
    # Make an overlay analysis using a subset of the rows
    result = gpd.overlay(grid[start_idx:end_idx], hel, how='intersection')
    # Append the overlay result to final GeoDataFrame
    final = final.append(result)
    # Update indices
    start_idx += b
    end_idx = start_idx + b
# Save the output as GeoJSON
outfp = "data/overlay_analysis_speedtest.geojson"
final.to_file(outfp, driver="GeoJSON")
