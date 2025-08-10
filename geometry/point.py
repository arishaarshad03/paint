
class Point:
    count =0
    def __init__(self, x=0.0, y=0.0):
        if isinstance (x,Point):
            self._x = x._x
            self._y = x._y
        else:
            self._x = x 
            self._y = y
        Point.count +=1
    # === Property for x ===
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # === Property for y ===
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # === Set Method ===
    def set_points(self, x=None, y=None):
        if x is not None:
            self.x = x  
        if y is not None:
            self.y = y

    # === Get Method ===
    def get_points(self):
        return (self.x, self.y)

    # === Copy Constructor ===
    @classmethod
    def copy(cls, otherPoint):
        return cls(otherPoint.x, otherPoint.y)

    # === String Representation ===
    def __str__(self):
        return f"(x={self.x}, y={self.y})"

    # === Operator Overload (+) ===
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        

    # === Show Method ===
    def show(self):
        print(self.__str__())

    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"
    
    def __eq__(self, otherPoint):
        return isinstance(otherPoint, Point) and self.x==otherPoint.x and self.y==otherPoint.y

    def distance (self,other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
    
    @classmethod
    def get_count (cls):
        return cls.count