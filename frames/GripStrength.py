import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class GripStrength(tk.Frame):
   
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.GripStrLeftText.get(1.0, tk.END).strip())
          self.GripStrLeftText.config(bg="white")
       except:
          self.GripStrLeftText.config(bg="red")
          validationSuccess = False

       try:
          float(self.GripStrRightText.get(1.0, tk.END).strip())
          self.GripStrRightText.config(bg="white")
       except:
          self.GripStrRightText.config(bg="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.GripStr = tk.Label(self)
       self.GripStr["text"] = "Grip Strength"
       self.GripStr.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.GripStrLeft = tk.Label(self.centerFrame)
       self.GripStrLeft["text"] = "Max. Left Hand(kg): "
       self.GripStrLeft.grid(row=1, column=0)

       self.GripStrLeftText = tk.Text(self.centerFrame)
       self.GripStrLeftText["height"] = 1
       self.GripStrLeftText["width"] = 5
       self.GripStrLeftText.bind("<Tab>", self.focus_next_window)
       self.GripStrLeftText.bind("<Shift-Tab>", self.focus_last_window)
       self.GripStrLeftText.grid(row=1, column=1)

       self.GripStrRight = tk.Label(self.centerFrame)
       self.GripStrRight["text"] = "Max. Right Hand(kg): "
       self.GripStrRight.grid(row=2, column=0)

       self.GripStrRightText = tk.Text(self.centerFrame)
       self.GripStrRightText["height"] = 1
       self.GripStrRightText["width"] = 5
       self.GripStrRightText.bind("<Tab>", self.focus_next_window)
       self.GripStrRightText.bind("<Shift-Tab>", self.focus_last_window)
       self.GripStrRightText.grid(row=2, column=1)

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

       self.GripStrLeftText.delete(1.0, tk.END)
       self.GripStrLeftText.insert(tk.END, person.gripStrengthLeft)

       self.GripStrRightText.delete(1.0, tk.END)
       self.GripStrRightText.insert(tk.END, person.gripStrengthRight)

   def saveData(self, person):
       person.gripStrengthLeft = self.GripStrLeftText.get(1.0, tk.END).strip()
       person.gripStrengthRight = self.GripStrRightText.get(1.0, tk.END).strip()
