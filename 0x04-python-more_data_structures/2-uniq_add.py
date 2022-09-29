#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    my_set.update(my_list)
    new_list = [elm for elm in my_set]
    res = 0
    for i in new_list:
        res += i
    res
