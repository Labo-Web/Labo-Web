from driving_map import DrivingMap

if __name__ == '__main__':
    map = DrivingMap()
    start_case = map.set_departure_point()
    map = map.set_default_route()


    for line in map.map_matrix:
        print line