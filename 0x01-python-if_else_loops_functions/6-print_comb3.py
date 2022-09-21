#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i < x:
            print("{:d}{:d}".format(i, x), end="")
            if i != 8:
                print(" ,", end="")
