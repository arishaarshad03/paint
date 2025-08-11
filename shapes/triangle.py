from geometry.point import Point
from drawing.pen import Pen

class Triangle:
    def __init__(self, point: Point, base= float, height= float):
        self.point = point
        self.base = base
        self.height = height

    def draw_triangle(self, canvas):
        x = self.point.x
        y = self.point.y
        base = self.base
        height = self.height

        pen = Pen(canvas, start_x= x, start_y=y)
        pen.line_to(Point(x+base , y))
        pen.line_to(Point(x+base/2, y-height))
        pen.line_to(Point(x,y))


