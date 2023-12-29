"""
CSAPX Lab 2: Fractal Antenna

A program that draws fractal antenna using two different recursive functions that use the turtle library.
The program also records the total length of the antenna.
n: The length of one "side" of the figure not the total length.
level: The amount of times the function will recurse.

author: Miles Sopchak
"""

import turtle


def main() -> None:
    """
    Propts the user to input n and level, then draws the fractal antenna implementing both strategies,
        recording the total side length of the figure.
    :return: None
    """
    n = input("Length of initial side: ")
    run = True
    while (run):
        run = False
        try:
            n = float(n)
            if (n <= 0):
                n = input("Please input a valid positive float: ")
                run = True

        except ValueError:
            n = input("Please input a valid positive float: ")
            run = True
    level = input("Number of levels: ")
    run = True
    while (run):
        run = False
        try:
            level = int(level)
            if (level <= 0):
                level = input("Please input a valid positive int: ")
                run = True

        except ValueError:
            level = input("Please input a positive valid int: ")
            run = True
    dist = 0.0
    for x in range(4):
        dist += strategy1(n,level)
        turtle.left(90)
    print("Strategy 1 - Antenna's length is " + str(dist) + " Units.")
    input("Hit enter to continue...")
    turtle.clear()
    print("Strategy 2 - Antenna's length is " + str(strategy2(n,level)) + " Units.")
    input("bye(press enter to end)")

def strategy1(n,level) -> float:
    """
    Draws one "side" of the fractal antenna by only drawing the perimeter of the shape. The base case draws a simple line
        then each level up rotates that line in a 5 line pattern that eventually draws the shape.
    :param n: The length of one "side" of the figure.
    :param level: The number of recursions to draw.
    :return: The total side length of the figure.
    """
    if (level == 1):
        turtle.forward(n)
        return n
    else:
        i = 0
        i += strategy1(n / 3,level - 1)
        turtle.left(90)
        i += strategy1(n / 3,level - 1)
        turtle.right(90)
        i += strategy1(n / 3,level - 1)
        turtle.right(90)
        i += strategy1(n / 3,level - 1)
        turtle.left(90)
        i += strategy1(n / 3,level - 1)
        return i

def strategy2(n,level) -> float:
    """
    Draws the fractal antenna square by square calling one level below itself to draw the center then positions the turtle
        in the center of each of the shapes sides and once again calls the function below to draw that side.
    :param n: The length of one "side" of the figure.
    :param level: The number of recursions to draw.
    :return: The total side length of the figure.
    """
    if (level == 1):
        for x in range(4):
            turtle.forward(n)
            turtle.left(90)
        return n * 4
    else:
        j = 0
        j += strategy2(n / 3,level - 1)
        box = n / pow(3,level - 1)
        for x in range(4):
            turtle.penup()
            turtle.forward(n/3)
            turtle.right(90)
            turtle.forward(n/3)
            turtle.left(90)
            turtle.pendown()
            j += strategy2(n / 3,level - 1)
            turtle.penup()
            turtle.right(90)
            turtle.backward(n/3)
            turtle.left(90)
            turtle.backward((n/3) - box)
            turtle.left(90)
            turtle.pendown()
        return j

if __name__ == '__main__':
    turtle.speed(0)
    turtle.left(45)
    main()