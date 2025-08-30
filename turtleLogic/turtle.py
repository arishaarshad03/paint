from drawing.pen import Pen
from geometry.point import Point
import math

class Turtle:
    def __init__(self, pen: Pen, start_x=0, start_y=0, angle=0):

        self._pen = self.validate_pen(pen)
        self._position = self.validate_position(Point(start_x, start_y))
        self.angle = angle           #validates angle using angle setter
        self._is_down = True         #checks whether pen is drawing

        #move pen to starting point without drawing anything
        self._pen.move_to(self._position)         #uses pen's move to method

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = self.validate_position(value)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("angle must be a number")
        self._angle = value % 360

    @property
    def is_down(self):
        return self._is_down
    
    # ---------- HELPER FUNCTIONS ----------
    def validate_pen (self, pen):
        if not isinstance(pen, Pen):
            raise TypeError ("pen should be an object of class pen")
        return pen
    
    def validate_position(self, point: Point):
        if not isinstance(point, Point):
            raise TypeError("position must be a Point")
        if not isinstance(point.x, (int, float)) or not isinstance(point.y, (int, float)):
            raise TypeError("position coordinates must be numbers")
        return point

    # ---------- MAIN FUNCTIONS ----------

    def forward (self, distance:float = 50):
        
        if not isinstance(distance,(int,float)):
            raise TypeError("distance must be a number")

        angle_rad = math.radians(self.angle)
        dx= distance * math.cos(angle_rad)      #change in x
        dy = distance * math.sin(angle_rad)     #change in y

        # create new Point
        new_point= Point(self.position.x + dx, self.position.y - dy)     
        #subtracting dy bcz in many graphics system y coordinate decreases going up and increases when going downwards

        if self.is_down:               # If pen is touching paper
            self._pen.line_to(new_point)    # Move to new spot AND draw a line
        else:                          # If pen is lifted
            self._pen.move_to(new_point)    # Just move without drawing

        self.position = new_point       #update turtle"s internal position

    def turn (self, angle:float):
        if not isinstance(angle, (int, float)):
            raise TypeError("angle must be a number")
        #turn left (positive) or turn right (neg) by a cretain angle
        self._angle = (self._angle + angle)%360

    def move_to(self, x, y):
        
        if not isinstance (x, (int, float)) or not isinstance (y, (int, float)):
            raise TypeError("x and y must be numbers")
        #Move turtle and pen to new position (without drawing)
        point = Point(x, y)
        self._pen.move_to(point)     #update pen's position
        self._position = point  # Update turtle's position too

    def reset(self):
        # Reset position and angle, and move pen.
        self._position = Point(0, 0)
        self._angle = 0
        self._pen.move_to(self._position)

    def pen_up(self):
        self._is_down = False

    def pen_down(self):
        self._is_down = True

    def __str__(self):
        return f"Turtle at {self._position}, angle {self._angle}°, pen {'down' if self.is_down else 'up'}"
