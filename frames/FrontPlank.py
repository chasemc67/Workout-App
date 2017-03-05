import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

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
       self.FrPlank.grid(row=0, column=0)

       self.FrPlankRate = tk.Label(self)
       self.FrPlankRate["text"] = "Rating(0-3): "
       self.FrPlankRate.grid(row=1, column=0)

       self.FrPlankRateText = tk.Text(self)
       self.FrPlankRateText["height"] = 1
       self.FrPlankRateText["width"] = 5
       self.FrPlankRateText.bind("<Tab>", self.focus_next_window)
       self.FrPlankRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.FrPlankRateText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData, self.validateInput)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.FrPlankRateText.delete(1.0, tk.END)
       self.FrPlankRateText.insert(tk.END, person.frontPlankRate)

   def saveData(self, person):
       person.frontPlankRate = self.FrPlankRateText.get(1.0, tk.END).strip()
