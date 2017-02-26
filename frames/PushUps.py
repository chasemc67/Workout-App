import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class PushUps(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")


   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.PushUp = tk.Label(self)
       self.PushUp["text"] = "Push Ups"
       self.PushUp.grid(row=0, column=0)

       self.PushUpNum = tk.Label(self)
       self.PushUpNum["text"] = "Number: "
       self.PushUpNum.grid(row=1, column=0)

       self.PushUpNumText = tk.Text(self)
       self.PushUpNumText["height"] = 1
       self.PushUpNumText["width"] = 5
       self.PushUpNumText.bind("<Tab>", self.focus_next_window)
       self.PushUpNumText.bind("<Shift-Tab>", self.focus_last_window)
       self.PushUpNumText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.PushUpNumText.delete(1.0, tk.END)
       self.PushUpNumText.insert(tk.END, person.pushUpNum)

   def saveData(self, person):
       person.pushUpNum = self.PushUpNumText.get(1.0, tk.END).strip()
