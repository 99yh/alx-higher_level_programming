#!/usr/bin/python3
def get_op(op):
    """gets the function related to an operator"""
    ops = "+-*/"
    func = [calc.add, calc.sub, calc.mul, calc.div]
    if op in ops and len(op) == 1:
        return func[ops.index(op)]
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = get_op(op)
    print("{} {} {} = {}".format(a, op, b, result(a, b)))
