def generate_neighborhood(coordinate, min_distance, max_distance):
    # given a coordinate, a minimum distance and a maximum distance
    # return a tuple of coordinates who are located between the min and maximal distances
    # from the initial coordinate inclusive.

    # Example: Given the coordinate (0,0), min=1 and max=2 we would return:
    # (0,2) , (-1,1), (0,1), (1,1), (-2,0), (-1,0), (1,0), (2,0), (-1,-1), (0,-1), (1,-1), (0,-2)

    if min_distance > max_distance:
        return ()

    dist = min_distance
    neighborhood = []
    while dist <= max_distance:
        # coord points 'north' first
        coord = (coordinate[0], coordinate[1] + dist)
        while coord[1] > coordinate[1]:
            coord = (coord[0]+1, coord[1]-1)
            neighborhood.append(coord)
        # coord should now be pointing 'east'
        while coord[0] > coordinate[0]:
            coord = (coord[0]-1, coord[1]-1)
            neighborhood.append(coord)
        # coord should now point 'south'
        while coord[1] < coordinate[1]:
            coord = (coord[0]-1, coord[1]+1)
            neighborhood.append(coord)
        # coord should no point 'west'
        while coord[0] < coordinate[0]:
            coord = (coord[0]+1, coord[1]+1)
            neighborhood.append(coord)
        dist += 1

    return tuple(neighborhood)
