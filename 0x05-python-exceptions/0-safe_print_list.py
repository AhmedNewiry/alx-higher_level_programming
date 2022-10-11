#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for item in range(x):
        try:
            num += 1
            print(f"{item[x]}", end="")
        except IndexError:
            break
    print("")
    return num
