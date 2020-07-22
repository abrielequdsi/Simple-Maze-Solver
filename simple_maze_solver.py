import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()
wn.bgcolor("#363636")
wn.title("Simple Maze Solver")
wn.setup(1132, 559)


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#fff")
        self.penup()
        self.speed(0)


class DBlue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#0f4c75")
        self.penup()
        self.speed(0)


class Turqoise(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#1dd3bd")
        self.penup()
        self.speed(0)


class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#fa1616")
        self.penup()
        self.speed(0)


grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+s  +       +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+               +                                 +",
    "+  ++++++++++  ++++++++++ ++  +++++++  +++++++ + ++",
    "+  +     +  +           +  +                 + +  +",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  +++ ++",
    "+        +                    +              +    +",
    "+ +++++ +++ +++ + + + +++    ++    ++    ++ ++ + ++",
    "+  +  +     +  +  ++++  +  +  +++++++++++++  + +  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++   +",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++    +       +++ +++ ++ ++++++ + ++ ++ ++   ++",
    "+      ++ ++++++ e+++     ++          ++    +++ +++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]


def setup_maze(grid):

    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):

            character = grid[y][x]

            screen_x = -556 + (x * 22)

            screen_y = 269 - (y * 22)

            if character == "+":

                maze.goto(screen_x, screen_y)
                maze.stamp()

                walls.append((screen_x, screen_y))

            if character == " " or character == "e":

                path.append((screen_x, screen_y))

            if character == "e":
                dblue.color("purple")

                dblue.goto(screen_x, screen_y)

                end_x, end_y = screen_x, screen_y
                dblue.stamp()
                dblue.color("#0f4c75")

            if character == "s":

                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        # pop next entry in the frontier queue an assign to x and y location
        x, y = frontier.popleft()

        if(x - 22, y) in path and (x - 22, y) not in visited:
            cell = (x - 22, y)

            solution[cell] = x, y
            turqoise.goto(cell)
            turqoise.stamp()
            frontier.append(cell)
            visited.add((x-22, y))

        if (x, y - 22) in path and (x, y - 22) not in visited:
            cell = (x, y - 22)
            solution[cell] = x, y
            turqoise.goto(cell)
            turqoise.stamp()
            frontier.append(cell)
            visited.add((x, y - 22))
            print(solution)

        if(x + 22, y) in path and (x + 22, y) not in visited:
            cell = (x + 22, y)
            solution[cell] = x, y
            turqoise.goto(cell)
            turqoise.stamp()
            frontier.append(cell)
            visited.add((x + 22, y))

        if(x, y + 22) in path and (x, y + 22) not in visited:
            cell = (x, y + 22)
            solution[cell] = x, y
            turqoise.goto(cell)
            turqoise.stamp()
            frontier.append(cell)
            visited.add((x, y + 22))

        dblue.goto(x, y)
        dblue.stamp()


def backRoute(x, y):
    red.goto(x, y)
    red.stamp()
    while (x, y) != (start_x, start_y):

        red.goto(solution[x, y])
        red.stamp()

        x, y = solution[x, y]


maze = Maze()
red = Red()
turqoise = Turqoise()
dblue = DBlue()


walls = []
path = []
visited = set()
frontier = deque()
solution = {}


setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
