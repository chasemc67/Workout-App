import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class HipHinge(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.HipHinge = tk.Label(self)
       self.HipHinge["text"] = "Hip Hinge"
       self.HipHinge.grid(row=0, column=0)

       self.HipHingeRate = tk.Label(self)
       self.HipHingeRate["text"] = "Rating(0-3): "
       self.HipHingeRate.grid(row=1, column=0)

       self.HipHingeRate = tk.Text(self)
       self.HipHingeRate["height"] = 1
       self.HipHingeRate["width"] = 5
       self.HipHingeRate.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)
