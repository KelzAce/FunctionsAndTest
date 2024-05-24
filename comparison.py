def compare_list(list1, list2):

    """
    Compare the contents of two lists. If the contents
   of the two lists are not equal, return the index of
   the first difference. If the contents of the two lists
   are equal, return -1
"""
    min_length = min(len(list1), len(list2))
    print(min_length, "here")



    for i in range(min_length):
        if list1[i] != list2[i]:
            return i
    
    if len(list1) != len(list2):
        return min_length
    
    return -1
            