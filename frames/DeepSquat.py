import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

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
       self.DeepSquat.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.DeepSquatRate = tk.Label(self.centerFrame)
       self.DeepSquatRate["text"] = "Rating(0-3): "
       self.DeepSquatRate.grid(row=1, column=0)

       self.DeepSquatRateText = tk.Text(self.centerFrame)
       self.DeepSquatRateText["height"] = 1
       self.DeepSquatRateText["width"] = 5
       self.DeepSquatRateText.bind("<Tab>", self.focus_next_window)
       self.DeepSquatRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.DeepSquatRateText.grid(row=1, column=1)

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

       self.DeepSquatRateText.delete(1.0, tk.END)
       self.DeepSquatRateText.insert(tk.END, person.deepSquatRate)

   def saveData(self, person):
       person.deepSquatRate = self.DeepSquatRateText.get(1.0, tk.END).strip()

