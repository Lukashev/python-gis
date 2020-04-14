import numpy as np
from shapely.geometry import Point, LineString


# convert arrays to Point shapes
def convert_to_point(elem):
    return Point(elem[0], elem[1])


# get [[origin_x, origin_y, destination_x, destination_y]]
coordinates = np.loadtxt('./data.txt', delimiter=';', encoding='UTF-8', skiprows=1, usecols=(5, 6, 7, 8))

orig_points = np.array([convert_to_point(xi) for xi in np.take(coordinates, [0, 1], axis=1)], dtype=Point)
dest_points = np.array([convert_to_point(xi) for xi in np.take(coordinates, [2, 3], axis=1)], dtype=Point)

# print(orig_points, dest_points)

# for xi in orig_points:
#     print(xi)
#
# for xi in dest_points:
#     print(xi)

line_strings = []
distances = []

for idx, origin in enumerate(orig_points):
    line_strings.append(LineString([origin, dest_points[idx]]))

for xi in line_strings:
    o_point = line_strings[0].interpolate(0.5)
    d_point = line_strings[1].interpolate(0.5)
    distances.append(o_point.distance(d_point))

print(distances)
