def without_duplicates(list):
    """
    Removes any duplicates from a list.

    Arguments: 
        list (list): The entered list that will have duplicates removed.

    Returns:
        no_dupe_list (list): The list with duplicates removed.
    """
    tracker_list = []
    no_dupe_list = []
    for i in list:
        if not i in tracker_list:
            no_dupe_list.append(i)
            tracker_list.append(i)
    return(no_dupe_list)

#print(without_duplicates([1,55,1,1,"hello",3,"b","gr","gr",0,0.1,0.6,0.1,1,54,54,2,3]))