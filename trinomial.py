#!/usr/bin/env python

import math
import numpy as np
import sys

def trinomial(*args):

    if len(args) != 3:
        return None
        
    a = args[0]
    b = args[1]
    c = args[2]
    args_type = np.array([a,b,c]).dtype

    if (args_type != float and args_type != int):
        return None

    if (a,b,c) == (0,0,0):
        return None

    if (a, b) == (0, 0):
        return tuple()

    if a == 0:
        result = -c / b
        return tuple((result,))


    delta = (b**2) - (4 * a * c)
    if delta > 0:
        result1 = (-b - math.sqrt(delta)) / (2 * a)
        result2 = (-b + math.sqrt(delta)) / (2 * a)
        return (result1, result2)
    elif delta == 0:
        result = -b / (2 * a) 
        return ((result,))
    else:
        return tuple()

def check1(*args):
    solution = trinomial(*args)
    if type(solution) != tuple:
        return (False,solution)
    else:
        return (True,solution)

if __name__ == "__main__":
    output = check1(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    print(output)
    