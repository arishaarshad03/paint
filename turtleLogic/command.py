
# ---------- SIMPLE COMMAND CLASSES ----------
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
     # Check for any invalid character first and rejects if any invalid character id found
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

    # ---------- COMPOSITE COMMANDS ----------

class SquareCommand:
    """Composite command: draws a square by repeating F+F+F+F+."""
    def name(self):
        return "Draw Square"

    def execute(self, turtle):
        pattern = "F+F+F+F+"
        commands = parse_command_string(pattern)
        # Run each command sequentially on the turtle
        for cmd in commands:
            cmd.run(turtle)

class ZigZagCommand:
    """Composite command: draws a zigzag pattern with F-F+F-F."""
    def name(self):
        return "Draw ZigZag"

    def execute(self, turtle):
        pattern = "F-F+F-F"
        commands = parse_command_string(pattern)
        for cmd in commands:
            cmd.run(turtle)

class CustomCommand:
    """Handles user-defined turtle command string at runtime."""
    def name(self):
        return "Custom Command"

    def execute(self, turtle):
        """
        Prompts user for a custom command string (F, +, -),
        parses it, and runs the commands from the turtle's current position.
        """
        # Ask user to enter a valid pattern like "F+F-F+"
        pattern = input("Enter custom command string (F = forward, + = turn right, - = turn left): ").strip()
        if not pattern:
            print("[Error] Empty command string!")
            return
        
        try:
            # Convert the pattern into a list of command objects
            commands = parse_command_string(pattern)

            # Run each command
            for cmd in commands:
                cmd.run(turtle)

        except ValueError as e:
            # Show warning for invalid characters in pattern
            print(f"[Warning] {e}")
