import tkinter as tk
from geometry.point import Point
from geometry.line import Line

class TKpanel(tk.Canvas):
    def __init__ (self,master= None, height=400, width=400, **kwargs):
        super().__init__(master, width=width, height= height, bg = "white", **kwargs)
        self.lines=[]

    def add_lines(self, p1:Point, p2:Point):
        line = Line (p1, p2)
        self.lines.append(line)
        print (f"line from {p1.get_points()} to {p2.get_points()}")
        self.draw()

    def draw(self):
        # draws all stored lines 
        self.delete("all")
        for line in self.lines:
            self.create_line(
                line.start.x, line.start.y,
                line.end.x, line.end.y,
                fill ='black', width =2
            )

    def clear_canvas(self):
        self.delete("all")
                             


