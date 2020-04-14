from shapely.geometry import Point, LineString, Polygon


# create simple Point
def create_point_geom(x_coord, y_coord):
    return Point(x_coord, y_coord)


# create LineString
def create_line_geom(shapely_list):
    try:
        for obj in shapely_list:
            if hasattr(obj, 'geom_type') is False or obj.geom_type != "Point":
                raise ValueError("List must contains only Point objects")
        return LineString(shapely_list)
    except Exception as error:
        print(error)


# create Polygon from List[tuples or Point]
def create_poly_geom(element_list):
    tmp = []
    for obj in element_list:
        elem = obj
        if hasattr(obj, 'geom_type') and obj.geom_type == "Point":
            elem = (elem.x, elem.y)
        tmp.append(elem)
    return Polygon(tmp)


point = create_point_geom(2.2, -4.5)

print(point)

line_string = create_line_geom([point, point])

print(line_string)

polygon1 = create_poly_geom([point, point, point])

print("Only Points: ", polygon1)

polygon2 = create_poly_geom([point, (1.2, -2.2), (2.2, 4.5)])

print("Mixed with tuples: ", polygon2)
