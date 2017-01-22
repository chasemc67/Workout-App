import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class GripStrength(tk.Frame):
   
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.GripStr = tk.Label(self)
       self.GripStr["text"] = "Grip Strength"
       self.GripStr.grid(row=0, column=0)

       self.GripStrLeft = tk.Label(self)
       self.GripStrLeft["text"] = "Max. Left Hand(kg): "
       self.GripStrLeft.grid(row=1, column=0)

       self.GripStrLeftText = tk.Text(self)
       self.GripStrLeftText["height"] = 1
       self.GripStrLeftText["width"] = 5
       self.GripStrLeftText.bind("<Tab>", self.focus_next_window)
       self.GripStrLeftText.grid(row=1, column=1)

       self.GripStrRight = tk.Label(self)
       self.GripStrRight["text"] = "Max. Right Hand(kg): "
       self.GripStrRight.grid(row=2, column=0)

       self.GripStrRightText = tk.Text(self)
       self.GripStrRightText["height"] = 1
       self.GripStrRightText["width"] = 5
       self.GripStrRightText.bind("<Tab>", self.focus_next_window)
       self.GripStrRightText.grid(row=2, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)

   def loadData(self, person):

       self.GripStrLeftText.delete(1.0, tk.END)
       self.GripStrLeftText.insert(tk.END, person.gripStrengthLeft)

       self.GripStrRightText.delete(1.0, tk.END)
       self.GripStrRightText.insert(tk.END, person.gripStrengthRight)

   def saveData(self, person):
       person.GripStrLeft = self.GripStrLeftText.get(1.0, tk.END)
       person.GripStrRight = self.GripStrRightText.get(1.0, tk.END)
