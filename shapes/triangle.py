from geometry.point import Point
from drawing.pen import Pen

class Triangle:
    def __init__(self, p1: Point, p2:Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw_triangle(self, canvas):
        pen = Pen(canvas, start_x=self.p1.x, start_y=self.p1.y)
        pen.line_to(self.p2)
        pen.line_to(self.p3)
        pen.line_to(self.p1)


