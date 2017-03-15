import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class PushUps(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")


   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.PushUpNumText.get(1.0, tk.END).strip())
          self.PushUpNumText.config(bg="white")
       except:
          self.PushUpNumText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.centerFrame = tk.Frame(self)

       self.PushUp = tk.Label(self.centerFrame)
       self.PushUp["text"] = "Push Ups"
       self.PushUp.grid(row=0, column=0)

       self.PushUpNum = tk.Label(self.centerFrame)
       self.PushUpNum["text"] = "Number: "
       self.PushUpNum.grid(row=1, column=0)

       self.PushUpNumText = tk.Text(self.centerFrame)
       self.PushUpNumText["height"] = 1
       self.PushUpNumText["width"] = 5
       self.PushUpNumText.bind("<Tab>", self.focus_next_window)
       self.PushUpNumText.bind("<Shift-Tab>", self.focus_last_window)
       self.PushUpNumText.grid(row=1, column=1)

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

       self.PushUpNumText.delete(1.0, tk.END)
       self.PushUpNumText.insert(tk.END, person.pushUpNum)

   def saveData(self, person):
       person.pushUpNum = self.PushUpNumText.get(1.0, tk.END).strip()
