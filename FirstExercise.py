import matplotlib.pyplot as plt
import numpy as np
import math


def graph():
    # Creating vectors X and Y
    x = np.linspace(-2, 2, 100)
    y = np.exp(np.power(np.sin(x), 3)) + np.power(x, 6) - 2 * np.power(x, 4) - np.power(x, 3) - 1

    fig = plt.figure(figsize=(14, 8))

    plt.title('Equation Plot')
    # Create the plot
    plt.plot(x, y)

    # Setting the range of the Y axis
    plt.ylim([-2, 2])

    # Creating grid
    plt.grid(alpha=.6, linestyle='--')

    # Axis Labels
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    # Show the plot
    plt.show()


def bisectionMethod():
    # Hardcoded the given function
    def func(x):
        return math.exp((math.sin(x)) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1.0

    def bisection(a, b, iterator=0):

        # Checking if right a and b where given
        if func(a) * func(b) >= 0:
            print("You not entered right values for a and b.\n")
            return
        c = 0
        while (abs(b - a)/2 >= 0.000005):
            iterator += 1
            # Find middle point
            c = (a + b) / 2
            # Check if middle point is root
            if (func(c) == 0.0):
                break
            # Deciding which points to choose for the next loop.
            if (func(c) * func(a) < 0):
                b = c
            else:
                a = c

        print("The value of root is : ", "%.5f" % c)
        print("The root got found after", "%d" % iterator, "loops.\n")

    # Here we choose the corresponding initial values
    a = -1.5
    b = 1.5
    bisection(a, b)


def newtonRaphsonMethod():
    # Hardcoded the given function
    def func(x):
        return math.exp((math.sin(x)) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1

    #  First derivative of the above function
    def derivFunc(x):
        return 6 * x ** 5 - 8 * x ** 3 - 3 * x ** 2 + 3 * (math.exp(math.sin(x) ** 3)) * math.sin(x) ** 2 * math.cos(x)

    def newtonRaphson(x, iterator=0):
        while True:
            temp = x
            h = func(x) / derivFunc(x)
            x = x - h

            iterator += 1
            if(abs(x - temp) <= 0.000005):
                break
        print("The value of the root is : ", "%.5f" % x)
        print("The root got found after", "%d" % iterator, "loops.\n")

    # Choosing starting value
    x0 = 0.1
    newtonRaphson(x0)


def secantMethod():
    # Hardcoded the given function
    def func(x):
        return math.exp((math.sin(x)) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1

    def secant(x1, x2, iterator=0):
        if (func(x1) * func(x2) >= 0):
            return
        while True:
            x0 = ((x1 * func(x2) - x2 * func(x1)) / (func(x2) - func(x1)))
            x1 = x2
            x2 = x0
            xtemp = ((x1 * func(x2) - x2 * func(x1)) / (func(x2) - func(x1)))
            iterator += 1
            if (abs(xtemp - x0) <= 0.000005):
                break
        print("The value of the root is : ", "%.5f" % x0)
        print("The root got found after", "%d" % iterator, "loops.\n")

    # initializing the values
    x1 = -1.2
    x2 = 0.1
    secant(x1, x2)


def main():
    # Calling each function
    graph()
    print("Bisection method results:")
    bisectionMethod()
    print("Newton-Raphson method results:")
    newtonRaphsonMethod()
    print("Secant method results:")
    secantMethod()


if __name__ == "__main__":
    main()
