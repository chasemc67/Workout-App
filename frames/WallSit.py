import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class WallSit(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSit = tk.Label(self)
       self.WallSit["text"] = "Wall Sit"
       self.WallSit.grid(row=0, column=0)

       self.WallSitTime = tk.Label(self)
       self.WallSitTime["text"] = "Time(sec.): "
       self.WallSitTime.grid(row=1, column=0)

       self.WallSitTime = tk.Text(self)
       self.WallSitTime["height"] = 1
       self.WallSitTime["width"] = 5
       self.WallSitTime.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)