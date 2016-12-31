import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

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

       self.Next = NextButton(self, controller)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)