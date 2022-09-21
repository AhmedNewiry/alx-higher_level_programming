#!/usr/bin/python3

for l in range(ord('z'), ord('a') - 1, -1):

        print("{:s}".format((chr(l - 32) if l % 2 != 0 else chr(l))), end="")
