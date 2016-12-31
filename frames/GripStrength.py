import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class GripStrength(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.GripStr = tk.Label(self)
       self.GripStr["text"] = "Grip Strength"
       self.GripStr.grid(row=0, column=0)

       self.GripStrLeft = tk.Label(self)
       self.GripStrLeft["text"] = "Max. Left Hand(kg): "
       self.GripStrLeft.grid(row=1, column=0)

       self.GripStrLeft = tk.Text(self)
       self.GripStrLeft["height"] = 1
       self.GripStrLeft["width"] = 5
       self.GripStrLeft.grid(row=1, column=1)

       self.GripStrRight = tk.Label(self)
       self.GripStrRight["text"] = "Max. Right Hand(kg): "
       self.GripStrRight.grid(row=2, column=0)

       self.GripStrRight = tk.Text(self)
       self.GripStrRight["height"] = 1
       self.GripStrRight["width"] = 5
       self.GripStrRight.grid(row=2, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)
