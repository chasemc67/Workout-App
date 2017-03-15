import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class FrontPlank(tk.Frame):
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.FrPlankRateText.get(1.0, tk.END).strip())
          self.FrPlankRateText.config(bg="white")
       except:
          self.FrPlankRateText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.FrPlank = tk.Label(self)
       self.FrPlank["text"] = "Front Plank"
       self.FrPlank.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.FrPlankRate = tk.Label(self.centerFrame)
       self.FrPlankRate["text"] = "Rating(0-3): "
       self.FrPlankRate.grid(row=1, column=0)

       self.FrPlankRateText = tk.Text(self.centerFrame)
       self.FrPlankRateText["height"] = 1
       self.FrPlankRateText["width"] = 5
       self.FrPlankRateText.bind("<Tab>", self.focus_next_window)
       self.FrPlankRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.FrPlankRateText.grid(row=1, column=1)

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

       self.FrPlankRateText.delete(1.0, tk.END)
       self.FrPlankRateText.insert(tk.END, person.frontPlankRate)

   def saveData(self, person):
       person.frontPlankRate = self.FrPlankRateText.get(1.0, tk.END).strip()
