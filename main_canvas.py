import tkinter as tk
from drawing.canvas import TKpanel
from drawing.pen import Pen
from geometry.point import Point
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle

def main():
    root = tk.Tk()
    root.title("Shapes")

    canvas = TKpanel(root, width=400, height=400)
    canvas.pack()

    # Create a Pen object
    pen = Pen(canvas, start_x=0, start_y=0)

    # Create and draw shapes
    square = Square(Point(50, 50), side=80.0)
    rectangle = Rectangle(Point(200, 50), length=100.0, width=60.0)
    triangle = Triangle(Point(150, 250), base=100, height=100)

    square.draw_square(pen)
    rectangle.draw_rectangle(pen)
    triangle.draw_triangle(pen)

    root.mainloop()

if __name__ == "__main__":
    main()

