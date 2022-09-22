#!/usr/bin/pyton3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) > 0:
        print("{}: {}".format(len(argv) - 1, "arguments" if len(argv) > 2 else "argument"))
        i = 0
        for arg in argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
