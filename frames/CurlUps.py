import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class CurlUps(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.CurlUp = tk.Label(self)
       self.CurlUp["text"] = "10cm Curl Ups"
       self.CurlUp.grid(row=0, column=0)

       self.CurlUpNum = tk.Label(self)
       self.CurlUpNum["text"] = "Number: "
       self.CurlUpNum.grid(row=1, column=0)

       self.CurlUpNum = tk.Text(self)
       self.CurlUpNum["height"] = 1
       self.CurlUpNum["width"] = 5
       self.CurlUpNum.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)
