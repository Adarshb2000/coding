#Name : Adarsh Baderia

def merge_intervals(intervals):
    """ @args : intervals is a list of tuples, where each tuple represents the
                (start_time, end_time) of an interval. Where start_time and end_time
                are both floats.
        @returns : a list of intervals, that merges any overlapping intervals
                    from the given list. The returned list is sorted order of start_time

        eg : [(1, 5), (2, 6), (9, 10), (10, 15), (7,8)] --> [(1,6), (7,8), (9, 15)]


    """

    merged_intervals = []
    # YOUR CODE GOES HERE
    if not intervals: return merged_intervals
    intervals.sort()
    
    merged_intervals.append(list(intervals[0]))
    
    for start, end in intervals:
        if merged_intervals[-1][-1] >= start:
            merged_intervals[-1][-1] = end
        
        else:
            merged_intervals.append([start, end])        

    merged_intervals = list(map(tuple, merged_intervals))


    return merged_intervals