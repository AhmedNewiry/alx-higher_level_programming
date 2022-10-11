#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for item in my_list:
        try:
            num += 1
            if x:
                print(f"{item}", end="")
                x -= 1
        except IndexError:
            break
    print("")
    return num