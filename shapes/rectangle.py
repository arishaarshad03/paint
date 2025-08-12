from geometry.point import Point
from drawing.pen import Pen

class Rectangle:
    def __init__(self, point:Point, length:float, width:float):
        self.point = point
        self.length= length
        self.width = width

    def draw_rectangle (self,pen: Pen):

        p1= self.point
        p2 = Point(p1.x + self.length, p1.y)
        p3= Point(p2.x, p2.y+self.width)
        p4= Point(p1.x,p1.y+self.width)

        pen.move_to(p1)
        pen.line_to(p2)
        pen.line_to(p3)
        pen.line_to(p4)
        pen.line_to(p1)


    