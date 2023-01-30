#!/usr/bin/env python

import math
import typing
import numpy as np
import sys

def trinomial(a:float, b:float, c:float):

    args_type = np.array([a,b,c]).dtype
    if args_type != float and args_type != int:
        return None

    if a == 0:
        result = -c / b
        return (result)

    delta = (b**2) - (4 * a * c)
    if delta > 0:
        result1 = (-b - math.sqrt(delta)) / (2 * a)
        result2 = (-b + math.sqrt(delta)) / (2 * a)
        return (result1, result2)
    elif delta == 0:
        result = -b / (2 * a) 
        return (result)
    else:
        return ()

def check2(trinomial: typing.Callable[[float,float,float],tuple],a,b,c):
    solution =  trinomial(a,b,c)
    if type(solution) != tuple:
        return False
    else:
        return True

def check1(a: float, b: float, c: float):
    solution = trinomial(a,b,c)
    if type(solution) != tuple:
        return False
    else:
        return (True,solution)

if __name__ == "__main__":
    output = check1(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    print(output)
