#!/usr/bin/python3
from calculator_1 import div, mul, add, sub
import sys
if __name__ == "main":
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op_list = {'+': "add", '-':"sub", '/':"div", '*':"mul"}
    if sys.argv[2] not in list(op_list.key()):
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
    process = op_list[sys.argv[2]]
    process = calculator_1.process
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = 
    {process(int(sys.argv[1]), int(sys.argv[3]))}")
