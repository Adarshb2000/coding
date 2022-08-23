#Name : Adarsh Baderia


def get_maximum_frequency_integer(list_of_integers):
    """@args : list_of_integers a list of integers , len(list_of_elements) >= 0
       @returns : the integer that occurs most frequently in the list_of_elements
                   if there are multiple such integers, returns the largest one.

        eg. [1,4,2,2,7,4, 18, 1] --> 4
        explaination : 4 and 2 both occurred 2 times, but 4 > 2
    """
    max_frequency_num = 0
    
    # YOUR CODE GOES HERE
    from collections import defaultdict as dd
    count = dd(int)
    for num in list_of_integers: count[num] += 1
    max_frequency_num = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]
   

    return max_frequency_num



