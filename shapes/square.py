from geometry.point import Point
from drawing.pen import Pen

class Square:
    def __init__(self, point:Point, side:float):
        self.point = point
        self.side = side

    def draw_square (self,pen:Pen):
        x = self.point.x
        y = self.point.y
        s = self.side

        p1= self.point
        p2 = Point(x+s , y)
        p3 = Point(x+s, y+s)
        p4 = Point(x, y+s)

        pen.move_to(p1)
        pen.line_to(p2)
        pen.line_to(p3)
        pen.line_to(p4)
        pen.line_to(p1)

