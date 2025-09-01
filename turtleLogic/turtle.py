from drawing.pen import Pen
from geometry.point import Point
import math

class Turtle:
    def __init__(self, pen: Pen, start_x=0, start_y=0, angle=0):

        self._pen = self.validate_pen(pen)          #stores pen after validation
        self._position = self.validate_position(Point(start_x, start_y))        #stores position after moving
        self._angle= self.validate_angle(angle)         #stores angle after validation
        self._is_down = True         #checks whether pen is drawing

        #move pen to starting point without drawing anything
        self._pen.move_to(self._position)         #uses pen's move to method

    # position setter & getter
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = self.validate_position(value)

    # angle setter & getter
    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
       self._angle = self.validate_angle(value)

    # is_down getter
    @property
    def is_down(self):
        return self._is_down
    
    # ---------- HELPER FUNCTIONS ----------
    def validate_pen (self, pen):
        """Ensure the pen is a valid Pen object."""
        if not isinstance(pen, Pen):
            raise TypeError ("pen should be an object of class pen")
        return pen
    
    def validate_position(self, point: Point):
        """Ensure the position is a valid Point with numeric coordinates."""
        if not isinstance(point, Point):
            raise TypeError("position must be a Point")
        if not isinstance(point.x, (int, float)) or not isinstance(point.y, (int, float)):
            raise TypeError("position coordinates must be numbers")
        return point

    def validate_angle (self, angle):
        """Ensure angle is numeric and normalized to [0, 360)."""
        if not isinstance (angle, (int, float)):
            raise TypeError("angle must be a number")
        return angle % 360

    # ---------- MAIN FUNCTIONS ----------

    def forward (self, distance:float = 50):
        # Moves the turtle forward in the current direction.

        if not isinstance(distance,(int,float)):
            raise TypeError("distance must be a number")

        angle_rad = math.radians(self.angle)    #changes angle to radians 
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
        # Rotates the turtle by the given angle.

        if not isinstance(angle, (int, float)):
            raise TypeError("angle must be a number")
        #turn left (positive) or turn right (neg) by a cretain angle

        self.angle = (self.angle + angle)%360

    def reset(self):
        # Reset position and angle, and move pen.
        self._position = Point(0, 0)
        self._angle = 0
        self._pen.move_to(self._position)

    def pen_up(self):
        """Lifts the pen — turtle will stop drawing while moving."""
        self._is_down = False

    def pen_down(self):
        """Lowers the pen — turtle will draw while moving."""
        self._is_down = True

    def __str__(self):
        return f"Turtle at {self._position}, angle {self._angle}°, pen {'down' if self.is_down else 'up'}"
