import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class PlankEnd(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")


   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.PlankTimeText.get(1.0, tk.END).strip())
          self.PlankTimeText.config(bg="white")
       except:
          self.PlankTimeText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Plank = tk.Label(self)
       self.Plank["text"] = "Front Plank"
       self.Plank.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.PlankTime = tk.Label(self.centerFrame)
       self.PlankTime["text"] = "Time(sec.)"
       self.PlankTime.grid(row=1, column=0)

       self.PlankTimeText = tk.Text(self.centerFrame)
       self.PlankTimeText["height"] = 1
       self.PlankTimeText["width"] = 5
       self.PlankTimeText.bind("<Tab>", self.focus_next_window)
       self.PlankTimeText.bind("<Shift-Tab>", self.focus_last_window)
       self.PlankTimeText.grid(row=1, column=1)

       self.centerFrame.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

   def loadData(self, person):

       self.PlankTimeText.delete(1.0, tk.END)
       self.PlankTimeText.insert(tk.END, person.plankTime)

   def saveData(self, person):
       person.plankTime = self.PlankTimeText.get(1.0, tk.END).strip()
