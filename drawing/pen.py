import math
from geometry.point import Point
from drawing.canvas import TKpanel

class Pen (Point):
    def __init__(self, canvas:TKpanel, start_x =0, start_y=0):
        super().__init__(start_x, start_y)
        self.canvas= canvas
        self.position = Point(start_x, start_y)
        self.angle = 0
        self.is_down= True     #drawing mode on
        # tracks how many lines are made
        self._lines_drawn =0

    def move_to (self,point: Point):
        self.position= point



    def line_to(self,point:Point):
        # draws a line from current position to that point 
        if isinstance (point, Point):
            self.canvas.add_lines(self.position, point)

        # move pen to end point (destination)
        self.position = point
        # update the line counter
        self._lines_drawn+=1

    def forward (self, distance:float):
        angle_rad = math.radians(self.angle)
        dx= distance * math.cos(angle_rad)      #change in x
        dy = distance * math.sin(angle_rad)     #change in y

        # create new Point
        new_point= Point(self.position.x + dx, self.position.y -dy)     
        #subtracting dy bcz in many graphics sys y coordinate decreases going up and increases when going downwards

        if self.is_down:               # If pen is touching paper
            self.draw_to(new_point)    # Move to new spot AND draw a line
        else:                          # If pen is lifted
            self.line_to(new_point)    # Just move without drawing


    def turn (self, angle:float):
        #turn left (positive) or turn right (neg) by a cretain angle
        self.angle = (self.angle + angle)%360
    

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


