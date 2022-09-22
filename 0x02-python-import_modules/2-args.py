#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0 arguments.")
    else:
        print("{:d} {:s}:".format(len(argv) - 1, "arguments" if len(argv) > 2 else "argument"))
        i = 0
        for arg in argv:
            if i != 0:
                print("{:d}: {:s}".format(i, arg))
            i += 1
