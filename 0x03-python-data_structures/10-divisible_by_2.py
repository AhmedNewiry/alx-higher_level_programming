#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list == False:
	return new_list
    new_list = my_list.copy()
    for i in new_list:
        if i % 2 == 0:
            new_list[i] = True
        else:
            new_lit[i] = False
    return new_list
