from .command import parse_command_string 
from drawing.pen import Pen
from .turtle import Turtle


class App:
    """
    App controller class that manages the drawing logic using Turtle and Pen.
    It receives a canvas, initializes a Turtle, and executes commands.
    """

    def __init__(self, canvas, start_x = 200, start_y=200):
        self.turtle = Turtle(Pen(canvas, start_x, start_y), start_x, start_y)
        

    def run(self, command_str, start_x = None, start_y = None):
        # Runs the given command string, optionally repositioning the turtle.
        if start_x is not None and start_y is not None:
            if not isinstance(start_x, (int,float)) or not isinstance(start_y,(int,float)):
                raise TypeError("start_x and start_y must be numbers")

            self.turtle.pen_up()
            self.turtle.move_to(start_x, start_y)
            self.turtle.pen_down()

        try:
            # Parse commands; will raise ValueError if any invalid character
            commands = parse_command_string(command_str)
        except ValueError as e:
            print(f"[Warning] {e}")
            return   # skip running any commands if invalid

        # runs valid commands
        for cmd in commands:
            cmd.run(self.turtle)
