import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class MBtoss(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SeatMB = tk.Label(self)
       self.SeatMB["text"] = "Seated Med. Ball Toss"
       self.SeatMB.grid(row=0, column=0)

       self.SeatMBDist = tk.Label(self)
       self.SeatMBDist["text"] = "Max. Distance(cm): "
       self.SeatMBDist.grid(row=1, column=0)

       self.SeatMBDist = tk.Text(self)
       self.SeatMBDist["height"] = 1
       self.SeatMBDist["width"] = 5
       self.SeatMBDist.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)