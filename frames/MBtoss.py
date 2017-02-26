import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class MBtoss(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SeatMB = tk.Label(self)
       self.SeatMB["text"] = "Seated Med. Ball Toss"
       self.SeatMB.grid(row=0, column=0)

       self.SeatMBDist = tk.Label(self)
       self.SeatMBDist["text"] = "Max. Distance(cm): "
       self.SeatMBDist.grid(row=1, column=0)

       self.SeatMBDistText = tk.Text(self)
       self.SeatMBDistText["height"] = 1
       self.SeatMBDistText["width"] = 5
       self.SeatMBDistText.bind("<Tab>", self.focus_next_window)
       self.SeatMBDistText.bind("<Shift-Tab>", self.focus_last_window)
       self.SeatMBDistText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.SeatMBDistText.delete(1.0, tk.END)
       self.SeatMBDistText.insert(tk.END, person.seatMBDist)

   def saveData(self, person):
       person.seatMBDist = self.SeatMBDistText.get(1.0, tk.END).strip()
