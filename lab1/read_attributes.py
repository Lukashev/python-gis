from shapely.geometry import LineString, Point, Polygon


# Get Shapely object centroid
def get_centroid(shape):
    return shape.centroid


# Get Shapely object area
def get_area(shape):
    return shape.area


# Get length of Polygon/LineString
def get_length(shape):
    if hasattr(shape, "geom_type") and shape.geom_type == "LineString":
        return shape.length
    if hasattr(shape, "geom_type") and shape.geom_type == "Polygon":
        return shape.exterior.length
    raise ValueError("Error: LineString or Polygon geometries required!")


point1 = Point(2.2, 4.5)
point2 = Point(3.4, 5.6)
point3 = Point(4.1, 3.2)

line_string = LineString([point1, point2, point3])
polygon = Polygon([point1, point2, point3])
print("LineString centroid: ", get_centroid(line_string))
print("Polygon centroid: ", get_centroid(polygon))

print("Polygon area: ", get_area(polygon))

print("LineString length: ", get_length(line_string))
print("Polygon external length: ", get_length(polygon))
# print(get_length(1))
