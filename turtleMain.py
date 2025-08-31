import tkinter as tk
from drawing.canvas import TKpanel
from turtleLogic.app import App

def main():
    try:
        root = tk.Tk()
        root.title("Turtle")

        # creates canvas
        canvas = TKpanel(root, width=400, height=400)
        canvas.pack()

        app = App(canvas)
        # ----- DRAWS SQUARE -----
        cmd1 = "F+F+F+F"    
        app.run(cmd1)       #starts at default position

        # draw zigzag
        cmd2= "f-f+f-f"
        app.run(cmd2, start_x=250,start_y=250)


        # invalid command
        cmd3 = "f*f*f"
        app.run(cmd3, start_x=300, start_y=300)     #will not execute

        root.mainloop()
    except Exception as e:
        # catches any kind of exception
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
