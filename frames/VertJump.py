import tkinter as tk

class VertJump(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.VertJump = tk.Label(self)
       self.VertJump["text"] = "Vertical Jump"
       self.VertJump.grid(row=0, column=0)

       self.VertJumpSR = tk.Label(self)
       self.VertJumpSR["text"] = "Standing Reach(ft/inch): "
       self.VertJumpSR.grid(row=1, column=0)

       self.VertJumpSR = tk.Text(self)
       self.VertJumpSR["height"] = 1
       self.VertJumpSR["width"] = 5
       self.VertJumpSR.grid(row=1, column=1)

       self.VertJumpBest = tk.Label(self)
       self.VertJumpBest["text"] = "Best Attempt(ft/inch): "
       self.VertJumpBest.grid(row=2, column=0)

       self.VertJumpBest = tk.Text(self)
       self.VertJumpBest["height"] = 1
       self.VertJumpBest["width"] = 5
       self.VertJumpBest.grid(row=2, column=1)

       self.NextE = tk.Button(self)
       self.NextE["text"] = "Next"
       self.NextE["fg"] = "black"
       self.NextE["command"] = lambda: controller.next_page()
       self.NextE.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitE = tk.Button(self)
       self.QuitE["text"] = "Quit"
       self.QuitE["fg"] = "black"
       self.QuitE["command"] = lambda: controller.show_frame("MainPage")
       self.QuitE.grid(row=3, column=2)