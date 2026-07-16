def find_median(num_list):
    """
    Finds the median of a list of numbers.

    Arguments: 
        num_list (list of floats): A list of numbers, of which the median will be found.

    Returns:
        median (float): The median of num_list.
    """
    sorted_list = num_list
    sorted_list.sort()
    half_length = int(len(num_list) / 2)
    print(half_length)
    if len(num_list) % 2 == 0:
        median = int(sorted_list[half_length])
    else:
        med1 = sorted_list[half_length]
        med2 = sorted_list[half_length + 1]
        median = (med2 + med1) / 2
    return(median)


#list = [2,0,1,4,3]
#print(find_median(list))