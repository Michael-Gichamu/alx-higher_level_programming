#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    bool_list = []
    for i in range(len_list):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
