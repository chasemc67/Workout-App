import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class DeepSquat(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.DeepSquatRateText.get(1.0, tk.END).strip())
          self.DeepSquatRateText.config(bg="white")
       except:
          self.DeepSquatRateText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.DeepSquat = tk.Label(self)
       self.DeepSquat["text"] = "Deep Squat"
       self.DeepSquat.grid(row=0, column=0)

       self.DeepSquatRate = tk.Label(self)
       self.DeepSquatRate["text"] = "Rating(0-3): "
       self.DeepSquatRate.grid(row=1, column=0)

       self.DeepSquatRateText = tk.Text(self)
       self.DeepSquatRateText["height"] = 1
       self.DeepSquatRateText["width"] = 5
       self.DeepSquatRateText.bind("<Tab>", self.focus_next_window)
       self.DeepSquatRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.DeepSquatRateText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData, self.validateInput)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.DeepSquatRateText.delete(1.0, tk.END)
       self.DeepSquatRateText.insert(tk.END, person.deepSquatRate)

   def saveData(self, person):
       person.deepSquatRate = self.DeepSquatRateText.get(1.0, tk.END).strip()

