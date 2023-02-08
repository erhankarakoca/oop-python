"""
    Create Point Class and
    Create Rectangle Class
"""
from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and \
                rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point1.x - self.point2.x) * (self.point1.y - self.point2.y))


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


def main():
    # Create rectangle object with random points
    gui_rectangle = GuiRectangle(Point(randint(0, 300), randint(0, 300)),
                                 Point(randint(10, 300), randint(10, 300)))

    # Print randomly generated rectangle coordinates
    print("Rectangle Coordinates: ",
          gui_rectangle.point1.x, ",",
          gui_rectangle.point1.y, "and",
          gui_rectangle.point2.x, ",",
          gui_rectangle.point2.y)

    # print(gui_rectangle.area())
    # myturtle = turtle.Turtle()
    # gui_rectangle.draw(canvas=myturtle)

    # Get point and area from user

    try:
        user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
        user_area = float(input("Guess rectangle area: "))
    except ValueError:
        print("The input must be float")

    # Print out the game result
    print(gui_rectangle.area())

    print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectangle))
    print("Your area was off by: ", gui_rectangle.area() - user_area)

    myturtle = turtle.Turtle()

    gui_rectangle.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)

    turtle.done()


if __name__ == '__main__':
    main()
