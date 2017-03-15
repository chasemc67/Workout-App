import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class WallSit(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.WallSitTimeText.get(1.0, tk.END).strip())
          self.WallSitTimeText.config(bg="white")
       except:
          self.WallSitTimeText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.centerFrame = tk.Frame(self)

       self.WallSit = tk.Label(self.centerFrame)
       self.WallSit["text"] = "Wall Sit"
       self.WallSit.grid(row=0, column=0)

       self.WallSitTime = tk.Label(self.centerFrame)
       self.WallSitTime["text"] = "Time(sec.): "
       self.WallSitTime.grid(row=1, column=0)

       self.WallSitTimeText = tk.Text(self.centerFrame)
       self.WallSitTimeText["height"] = 1
       self.WallSitTimeText["width"] = 5
       self.WallSitTimeText.bind("<Tab>", self.focus_next_window)
       self.WallSitTimeText.bind("<Shift-Tab>", self.focus_last_window)
       self.WallSitTimeText.grid(row=1, column=1)

       self.centerFrame.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

   def loadData(self, person):

       self.WallSitTimeText.delete(1.0, tk.END)
       self.WallSitTimeText.insert(tk.END, person.wallSitTime)

   def saveData(self, person):
       person.wallSitTime = self.WallSitTimeText.get(1.0, tk.END).strip()
