#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    my_set.update(my_list)
    return [elm for elm in my_set]
