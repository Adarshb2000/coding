#Name : Adarsh Baderia

def get_minimum_distance_elements(itegers):
    """ given a list of integers, return a list of integers as tuples with the minimum absolute difference, sorted in ascending order)
        eg.  [8, 3, 5, 1, 2] --> [(1,2), (2,3)] """

    minimum_distance_elements = []
    # your code goes here
    itegers.sort()
    from math import inf
    currMin = inf
    for i in range(len(itegers) - 1):
        diff = itegers[i + 1] - itegers[i]
        if diff == currMin:
            minimum_distance_elements.append((itegers[i], itegers[i + 1]))
        elif diff < currMin:
            minimum_distance_elements = [(itegers[i], itegers[i + 1])]
            currMin = diff
    
    return minimum_distance_elements
