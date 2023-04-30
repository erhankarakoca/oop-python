from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and promp for color
colors = {"white" : (255,255,255), "black" : (0,0,0)}
canvas_color = input("Enter canvas color (white or black): ")

#Create canvas with user input
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What shape do u want to draw ? (Please push enter  if want to quit.) ")
    #Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should be rectangle have ? "))
        green = int(input(" How much green ? "))
        blue = int(input("What about the blue ? "))

        # Now create rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color =(red,green,blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter width of the square: "))
        red = int(input("How much red should be square have ? "))
        green = int(input(" How much green ? "))
        blue = int(input("What about the blue ? "))

        # Now create rectangle
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color =(red,green,blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make('canvas.png')

