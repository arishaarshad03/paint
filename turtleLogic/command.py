
# ---------- COMMAND CLASSES ----------
class ForwardCommand:
    def __init__(self, distance=50):
        if not isinstance(distance, (float, int)):
            raise TypeError("distance must be a number")
        self.distance = distance

    def run (self,turtle):
        turtle.forward(self.distance)

class TurnRightCommand:
    def __init__ (self, angle = 90):
        if not isinstance(angle, (float, int)):
            raise TypeError("angle must be a number")
        self.angle = angle
    
    def run (self, turtle):
        turtle.turn(self.angle)

class TurnLeftCommand:
    def __init__(self,angle = 90):
        if not isinstance(angle, (float, int)):
            raise TypeError("angle must be a number")
        self.angle = angle 

    def run(self, turtle):
        turtle.turn (-self.angle)

# ---------- PARSER FUNCTION ----------
def parse_command_string(command_str):
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
            commands.append(TurnLeftCommand())
        elif ch == "-":
            commands.append(TurnRightCommand())
    return commands
