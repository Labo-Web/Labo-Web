from driving_map import DrivingMap

if __name__ == '__main__':
    currentmap = DrivingMap()
    
    start_case = currentmap.set_departure_point()
    
    currentmap.set_default_route()


    for line in currentmap.map_matrix:
        print line