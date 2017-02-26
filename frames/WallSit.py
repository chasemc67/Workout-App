import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class WallSit(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSit = tk.Label(self)
       self.WallSit["text"] = "Wall Sit"
       self.WallSit.grid(row=0, column=0)

       self.WallSitTime = tk.Label(self)
       self.WallSitTime["text"] = "Time(sec.): "
       self.WallSitTime.grid(row=1, column=0)

       self.WallSitTimeText = tk.Text(self)
       self.WallSitTimeText["height"] = 1
       self.WallSitTimeText["width"] = 5
       self.WallSitTimeText.bind("<Tab>", self.focus_next_window)
       self.WallSitTimeText.bind("<Shift-Tab>", self.focus_last_window)
       self.WallSitTimeText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.WallSitTimeText.delete(1.0, tk.END)
       self.WallSitTimeText.insert(tk.END, person.wallSitTime)

   def saveData(self, person):
       person.wallSitTime = self.WallSitTimeText.get(1.0, tk.END).strip()
