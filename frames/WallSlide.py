import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class WallSlide(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSlide = tk.Label(self)
       self.WallSlide["text"] = "Wall Slide"
       self.WallSlide.grid(row=0,column=0)

       self.WallSlideRate = tk.Label(self)
       self.WallSlideRate["text"] = "Rating(0-3): "
       self.WallSlideRate.grid(row=1, column=0)

       self.WallSlideRate = tk.Text(self)
       self.WallSlideRate["height"] = 1
       self.WallSlideRate["width"] = 5
       self.WallSlideRate.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)