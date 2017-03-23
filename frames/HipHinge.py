import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class HipHinge(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.HipHingeRateText.get(1.0, tk.END).strip())
          self.HipHingeRateText.config(bg="white")
       except:
          self.HipHingeRateText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.HipHinge = tk.Label(self)
       self.HipHinge["text"] = "Hip Hinge"
       self.HipHinge.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.HipHingeRate = tk.Label(self.centerFrame)
       self.HipHingeRate["text"] = "Rating(0-3): "
       self.HipHingeRate.grid(row=1, column=0)

       self.HipHingeRateText = tk.Text(self.centerFrame)
       self.HipHingeRateText["height"] = 1
       self.HipHingeRateText["width"] = 5
       self.HipHingeRateText.bind("<Tab>", self.focus_next_window)
       self.HipHingeRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.HipHingeRateText.grid(row=1, column=1)

       self.centerFrame.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller, self.saveData)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

   def loadData(self, person):

       self.HipHingeRateText.delete(1.0, tk.END)
       self.HipHingeRateText.insert(tk.END, person.hipHingeRate)

   def saveData(self, person):
       person.hipHingeRate = self.HipHingeRateText.get(1.0, tk.END).strip()
