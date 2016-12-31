import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class PushUps(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.PushUp = tk.Label(self)
       self.PushUp["text"] = "Push Ups"
       self.PushUp.grid(row=0, column=0)

       self.PushUpNum = tk.Label(self)
       self.PushUpNum["text"] = "Number: "
       self.PushUpNum.grid(row=1, column=0)

       self.PushUpNum = tk.Text(self)
       self.PushUpNum["height"] = 1
       self.PushUpNum["width"] = 5
       self.PushUpNum.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)