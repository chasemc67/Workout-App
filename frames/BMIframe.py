import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class BMIframe(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = "BMI"
       self.BMIresult.grid(row=1, column=0)

       self.BMIresult = tk.Text(self)
       self.BMIresult["height"] = 1
       self.BMIresult["width"] = 5
       self.BMIresult.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def saveData(self, person):
      print("Saving Data:")
      print(person.height)
      person.height = 100
      print(person.height)

