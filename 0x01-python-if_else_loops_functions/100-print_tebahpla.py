#!/usr/bin/python3

for le in range(ord('z'), ord('a') - 1, -1):
    print("{:s}".format((chr(le - 32) if le % 2 != 0 else chr(le))), end="")
