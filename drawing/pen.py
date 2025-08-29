from geometry.point import Point
from drawing.canvas import TKpanel

class Pen (Point):
    def __init__(self, canvas:TKpanel, start_x =0, start_y=0):
        super().__init__(start_x, start_y)
        self.canvas= canvas
        self._lines_drawn=0

    def move_to (self,point: Point):
        self.x = point.x
        self.y = point.y

    def line_to(self,point:Point):
        # draws a line from current position to that point 
        if isinstance (point, Point):
            self.canvas.add_lines(Point(self.x, self.y), point)

        # move pen to end point (destination)
        self.x = point.x
        self.y = point.y
        self._lines_drawn +=1
        

    def __str__(self):
        return f"pen at position ({self.x},{self.y})"

    def __repr__(self):
        return f"Pen(x={self.x}, y={self.y})"
    
    def reset(self):
        #Reset pen position to (0, 0) without drawing
        self.x = 0
        self.y = 0
    def __len__(self):
        #Return the number of lines drawn by the pen
        return self._lines_drawn


