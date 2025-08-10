import tkinter as tk
from drawing.canvas import TKpanel
from geometry.point import Point
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
def main():
    root = tk.Tk()
    root.title("shapes")

    canvas = TKpanel(root, width=400, height=400)
    canvas.pack()

    # Create and draw shapes
    square = Square (Point(50,50) ,side=80.0)
    rectangle = Rectangle(Point(200,50), length=100.0, width=60.0)
    triangle = Triangle(Point(100,200), p2=Point(150,300), p3= Point(50,300))

    square.draw_square(canvas)
    rectangle.draw_rectangle(canvas)
    triangle.draw_triangle(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
