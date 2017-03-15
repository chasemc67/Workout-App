import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class RMtest(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.RMTestExAText.get(1.0, tk.END).strip())
          self.RMTestExAText.config(bg="white")
       except:
          self.RMTestExAText.config(bg="red")
          validationSuccess = False

       try:
          float(self.RMTestExAWeightText.get(1.0, tk.END).strip())
          self.RMTestExAWeightText.config(bg="white")
       except:
          self.RMTestExAWeightText.config(bg="red")
          validationSuccess = False

       try:
          float(self.RMTestExBText.get(1.0, tk.END).strip())
          self.RMTestExBText.config(bg="white")
       except:
          self.RMTestExBText.config(bg="red")
          validationSuccess = False

       try:
          float(self.RMTestExBWeightText.get(1.0, tk.END).strip())
          self.RMTestExBWeightText.config(bg="white")
       except:
          self.RMTestExBWeightText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RepMaxTest = tk.Label(self)
       self.RepMaxTest["text"] = "1 Rep Max.(Tested)"
       self.RepMaxTest.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.RMTestExA = tk.Label(self.centerFrame)
       self.RMTestExA["text"] = "Exercise: "
       self.RMTestExA.grid(row=1, column=0)

       self.RMTestExAText = tk.Text(self.centerFrame)
       self.RMTestExAText["height"] = 1
       self.RMTestExAText["width"] = 10
       self.RMTestExAText.bind("<Tab>", self.focus_next_window)
       self.RMTestExAText.bind("<Shift-Tab>", self.focus_last_window)
       self.RMTestExAText.grid(row=1, column=1)

       self.RMTestExAWeight = tk.Label(self.centerFrame)
       self.RMTestExAWeight["text"] = "1RM(kg): "
       self.RMTestExAWeight.grid(row=1, column=2)

       self.RMTestExAWeightText = tk.Text(self.centerFrame)
       self.RMTestExAWeightText["height"] = 1
       self.RMTestExAWeightText["width"] = 10
       self.RMTestExAWeightText.bind("<Tab>", self.focus_next_window)
       self.RMTestExAWeightText.bind("<Shift-Tab>", self.focus_last_window)
       self.RMTestExAWeightText.grid(row=1, column=3)

       self.RMTestExB = tk.Label(self.centerFrame)
       self.RMTestExB["text"] = "Exercise: "
       self.RMTestExB.grid(row=2, column=0)

       self.RMTestExBText = tk.Text(self.centerFrame)
       self.RMTestExBText["height"] = 1
       self.RMTestExBText["width"] = 10
       self.RMTestExBText.bind("<Tab>", self.focus_next_window)
       self.RMTestExBText.bind("<Shift-Tab>", self.focus_last_window)
       self.RMTestExBText.grid(row=2, column=1)

       self.RMTestExBWeight = tk.Label(self.centerFrame)
       self.RMTestExBWeight["text"] = "1RM(kg): "
       self.RMTestExBWeight.grid(row=2, column=2)

       self.RMTestExBWeightText = tk.Text(self.centerFrame)
       self.RMTestExBWeightText["height"] = 1
       self.RMTestExBWeightText["width"] = 10
       self.RMTestExBWeightText.bind("<Tab>", self.focus_next_window)
       self.RMTestExBWeightText.bind("<Shift-Tab>", self.focus_last_window)
       self.RMTestExBWeightText.grid(row=2, column=3)

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

       self.RMTestExAText.delete(1.0, tk.END)
       self.RMTestExAText.insert(tk.END, person.RMTestExA)

       self.RMTestExAWeightText.delete(1.0, tk.END)
       self.RMTestExAWeightText.insert(tk.END, person.RMTestExAWeight)

       self.RMTestExBText.delete(1.0, tk.END)
       self.RMTestExBText.insert(1.0, person.RMTestExB)

       self.RMTestExBWeightText.delete(1.0, tk.END)
       self.RMTestExBWeightText.insert(1.0, person.RMTestExBWeight)

   def saveData(self, person):
       person.RMTestExA = self.RMTestExAText.get(1.0, tk.END).strip()
       person.RMTestExAWeight = self.RMTestExAWeightText.get(1.0, tk.END).strip()
       person.RMTestExB = self.RMTestExBText.get(1.0, tk.END).strip()
       person.RMTestExBWeight = self.RMTestExBWeightText.get(1.0, tk.END).strip()
