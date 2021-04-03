import math
from numpy import random


def newtonRaphsonMethod():
    def func(x):
        return 94 * (math.cos(x)) ** 3 - 24 * math.cos(x) + 177 * (math.sin(x)) ** 2 - 108 * (math.sin(x)) ** 4 - 72 * (
            math.cos(x)) ** 3 * (math.sin(x)) ** 2 - 65

    #  First derivative of the above function

    def derivFunc(x):
        return (216 * (math.cos(x)) ** 2 - 432 * (math.cos(x))) * (math.sin(x)) ** 3 + (
                -144 * (math.cos(x)) ** 4 - 282 * (math.cos(x)) ** 2 + 354 * (math.cos(x)) + 24) * math.sin(x)

    #  First derivative of the above function

    def secondDerivFunc(x):
        return (432 - 432 * math.cos(x)) * (math.sin(x)) ** 4 + (
                1224 * (math.cos(x)) ** 3 - 1296 * (math.cos(x)) ** 2 + 564 * math.cos(x) - 354) * (
                   math.sin(x)) ** 2 - 144 * (math.cos(x)) ** 5 - 282 * (math.cos(x)) ** 3 + 354 * (
                   math.cos(x)) ** 2 + 24 * math.cos(x)

    def newtonRaphson(x, iterator=0):
        while True:
            temp = x
            h = func(x) / derivFunc(x) + 0.5 * (((func(x)) ** 2 * (secondDerivFunc(x))) / derivFunc(x) ** 3)
            x = x - h

            iterator += 1
            if (abs(x - temp) <= 0.000005):
                break
        print("The value of the root is : ", "%.5f" % x)
        print("The root got found after", "%d" % iterator, "loops.\n")

    # Choosing starting value
    x0 = 2.2
    newtonRaphson(x0)


def bisectionMethod():
    # Hardcoded the given function
    def func(x):
        return 94 * (math.cos(x)) ** 3 - 24 * math.cos(x) + 177 * (math.sin(x)) ** 2 - 108 * (math.sin(x)) ** 4 - 72 * (
            math.cos(x)) ** 3 * (math.sin(x)) ** 2 - 65

    def bisection(a, b, iterator=0):
        tempc = 0
        while True:
            iterator += 1
            c = random.uniform(a, b)

            if (func(c) == 0.0 or abs(c - tempc) < 0.000005):
                break

            # Deciding which points to choose for the next loop.
            if (func(c) * func(a) < 0):
                b = c
                tempc = c
            else:
                a = c
                tempc = c

        print("The value of the root is : ", "%.5f" % c)
        print("The root got found after", "%d" % iterator, "loops.\n")
    a = 2.3
    b = 2.4
    bisection(a, b)


def secantMethod():
    def func(x):
        return 94 * (math.cos(x)) ** 3 - 24 * math.cos(x) + 177 * (math.sin(x)) ** 2 - 108 * (math.sin(x)) ** 4 - 72 * (
            math.cos(x)) ** 3 * (math.sin(x)) ** 2 - 65

    def secant(x1, x2, x3, iterator=0):
        while True:
            q = func(x1) / func(x2)
            r = func(x3) / func(x2)
            s = func(x3) / func(x1)

            x0 = x3 - ((r * (r - q) * (x3 - x2) + (1 - r) * s * (x3 - x1)) / ((q - 1) * (r - 1) * (s - 1)))
            x1 = x2
            x2 = x3
            x3 = x0
            iterator += 1

            xtemp = x3 - ((r * (r - q) * (x3 - x2) + (1 - r) * s * (x3 - x1)) / ((q - 1) * (r - 1) * (s - 1)))

            if (abs(xtemp - x0) < 0.000005):
                break

        print("The value of the root is : ", "%.5f" % x0)
        print("The root got found after", "%d" % iterator, "loops.\n")

    # Initializing the values
    x1 = 2
    x2 = 2.2
    x3 = 2.3
    secant(x1, x2, x3)


def main():
    # Calling each function
    print("Bisection method results:")
    bisectionMethod()
    print("Newton-Raphson method results:")
    newtonRaphsonMethod()
    print("Secant method results:")
    secantMethod()


if __name__ == "__main__":
    main()
