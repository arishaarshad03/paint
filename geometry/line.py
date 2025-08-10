from geometry.point import Point
class Line:
    def __init__ (self, start:Point, end:Point):
        self._start= start
        self._end= end
    @property
    def start (self):
        return self._start

    @start.setter
    def start (self, newstart):
        self._start = newstart
    @property
    def end (self):
        return self._end

    @end.setter
    def end (self, end):
        self._end = end
    
    def set_line(self, start= None, end = None):
        if start is not None:
            self.start=start
        if end is not None:
            self.end = end

    def get_line(self):
        return f"starting point:{self.start}\n end point:{self.end}"
    
    def length (self):
        return self.start.distance(self.end)
    
    def __str__(self):
        return f"Line({self.start} → {self.end})"
    
