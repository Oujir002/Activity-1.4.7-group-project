# main.py

import tkinter as tk 

# Window class to handle all inputs and represent visuals
class Window(tk.Frame): 
    # initialization of window
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        # configures frame to size of 100,100
        self.config(width=100, height=100)
        # binds and sets location that will be handled
        self.bind("<Button-1>", self.handle_mouse_click) 
        self.pack()
 
    # a debugging function to show where user clicked
    def handle_mouse_click(self, event): 
        position = "(%s, %s)" % (event.x, event.y)
        print("clicked @: " + position)

# creates the window
app = Window(master=tk.Tk())
app.mainloop()