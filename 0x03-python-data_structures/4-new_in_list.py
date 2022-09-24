#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or id > (len(my_list) - 1):
        return my_list
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
