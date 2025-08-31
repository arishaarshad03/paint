
# ---------- COMMAND CLASSES ----------
class ForwardCommand:
    # Represents the 'F' command to move the turtle forward.

    def __init__(self, distance=50):
        if not isinstance(distance, (float, int)):
            raise TypeError("distance must be a number")
        self.distance = distance

    def run (self,turtle):
        #  Executes the command by calling turtle.forward().
        turtle.forward(self.distance)

class TurnRightCommand:
    # Represents the '+' command to turn the turtle right.
    def __init__ (self, angle = 90):
        if not isinstance(angle, (float, int)):
            raise TypeError("angle must be a number")
        self.angle = angle
    
    def run (self, turtle):
        # Executes the command by calling turtle.turn()
        turtle.turn(self.angle)

class TurnLeftCommand:
    # Represents the '-' command to turn the turtle left.
    def __init__(self,angle = 90):
        if not isinstance(angle, (float, int)):
            raise TypeError("angle must be a number")
        self.angle = angle 

    def run(self, turtle):
        # Executes the command by calling turtle.turn() with negative angle.
        turtle.turn (-self.angle)

# ---------- PARSER FUNCTION ----------
def parse_command_string(command_str):
    """
    Parses a string of turtle drawing commands and converts them
    into a list of executable Command objects.

    Commands supported:
        - 'F' or 'f' → Move forward
        - '+'        → Turn right
        - '-'        → Turn left
    """
     
    commands = []
     # Check for any invalid character first
    valid_chars = {"F", "+", "-"}
    for ch in command_str.upper():
        if ch not in valid_chars:
            raise ValueError(f"Unknown command: '{ch}' — entire command ignored")

    # If all characters are valid, convert to command objects
    for ch in command_str:
        ch_upper = ch.upper()  # Converts to uppercase if user inputs "f" instead of "F"
        if ch_upper == "F":
            commands.append(ForwardCommand())
        elif ch == "+":
            commands.append(TurnRightCommand())
        elif ch == "-":
            commands.append(TurnLeftCommand())
    return commands
