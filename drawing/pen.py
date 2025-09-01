from geometry.point import Point
from drawing.canvas import TKpanel

class Pen:
    """
    Pen class handles drawing on a canvas.
    """
    def __init__(self, canvas:TKpanel):
        self.canvas= canvas
        self._cp=Point(0,0)     # Start position at (0, 0)
        self._lines_drawn=0

    def move_to (self,point):
        # Moves the pen to a new position without drawing.
        self._cp=point
        
    def line_to(self,point:Point):
        # Draws a line from the current position to the given point,
        # then moves the pen to that point 
       self.canvas.add_lines(self._cp, point)
       self._cp = point              
          
    def __str__(self):
        return f"pen at position ({self._cp.x}, {self._cp.y})"

    def __repr__(self):
       return f"Pen(x={self._cp.x}, y={self._cp.y})"
    
    def reset(self):
         # Reset pen position to (0,0) without drawing
        self._cp = Point(0, 0)

    def __len__(self):
        #Return the number of lines drawn by the pen
        return self._lines_drawn


