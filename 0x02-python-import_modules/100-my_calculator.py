#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import div, mul, add, sub
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op_list = {'+': "add", '-':"sub", '/':"div", '*':"mul"}
    if sys.argv[2] not in list(op_list.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {sys.argv[2]} {}".format(a, b, op_list[sys.argv[2]](a, b)))
