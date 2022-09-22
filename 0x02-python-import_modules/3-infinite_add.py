#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print(argv[1])
    else:
        i = 0
        res = 0
        for arg in argv:
            if i != 0:
                res += int(arg)
            i += 1
        print(res)
