import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

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
       self.HipHinge.grid(row=0, column=0)

       self.HipHingeRate = tk.Label(self)
       self.HipHingeRate["text"] = "Rating(0-3): "
       self.HipHingeRate.grid(row=1, column=0)

       self.HipHingeRateText = tk.Text(self)
       self.HipHingeRateText["height"] = 1
       self.HipHingeRateText["width"] = 5
       self.HipHingeRateText.bind("<Tab>", self.focus_next_window)
       self.HipHingeRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.HipHingeRateText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData, self.validateInput)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.HipHingeRateText.delete(1.0, tk.END)
       self.HipHingeRateText.insert(tk.END, person.hipHingeRate)

   def saveData(self, person):
       person.hipHingeRate = self.HipHingeRateText.get(1.0, tk.END).strip()
