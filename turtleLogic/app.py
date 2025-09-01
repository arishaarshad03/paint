import tkinter as tk
from drawing.canvas import TKpanel
from drawing.pen import Pen
from .turtle import Turtle
from .command import SquareCommand, ZigZagCommand, CustomCommand  # your composite commands

class App:
    """
        Initialize the application:
        - Creates a Tkinter window
        - Initializes a canvas for drawing
        - Creates a turtle with a pen
        - Loads predefined commands
        - Launches the command interface
        """
    
    def __init__(self):
        # Setup GUI window
        self.root = tk.Tk()
        self.root.title("Turtle")

        # Setup canvas and pack
        self.canvas = TKpanel(self.root, width=400, height=400)
        self.canvas.pack()

        # Create turtle and command list
        self.turtle = Turtle(Pen(self.canvas), 200, 200)
        self.commands = [SquareCommand(), ZigZagCommand(), CustomCommand()]

        # Run the launcher interface
        self.run()

        # Keep GUI alive
        self.root.mainloop()

    def run(self):
        """
        Displays a command menu in the terminal,
        takes the user's choice, and executes the selected command.
        """
        # Display options
        print("Available drawing commands:")
        for i, cmd in enumerate(self.commands):         #enumerate loop over a list & get index of each item and get index each time
            print(f"{i + 1}. {cmd.name()}")
            # {i + 1} makes the numbering start at 1 (instead of 0) & cmd.name() calls the .name() method on the command object to get its display name.

        try:
            choice = int(input(f"Choose a command (1 to {len(self.commands)}): "))

            if 1 <= choice <= len(self.commands):       #checks if input is valid
                # execute the selected command
                self.commands[choice - 1].execute(self.turtle)

            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

        

