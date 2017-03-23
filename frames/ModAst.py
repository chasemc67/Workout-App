import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class ModAst(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.ModAstLoadAText.get(1.0, tk.END).strip())
          self.ModAstLoadAText.config(bg="white")
       except:
          self.ModAstLoadAText.config(bg="red")
          validationSuccess = False

       try:
          float(self.ModAstLoadBText.get(1.0, tk.END).strip())
          self.ModAstLoadBText.config(bg="white")
       except:
          self.ModAstLoadBText.config(bg="red")
          validationSuccess = False

       try:
          float(self.ModAstHRText.get(1.0, tk.END).strip())
          self.ModAstHRText.config(bg="white")
       except:
          self.ModAstHRText.config(bg="red")
          validationSuccess = False

       try:
          float(self.ModAstCapacityText.get(1.0, tk.END).strip())
          self.ModAstCapacityText.config(bg="white")
       except:
          self.ModAstCapacityText.config(bg="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ModAst = tk.Label(self)
       self.ModAst["text"] = "Modified Astrand"
       self.ModAst.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.ModAstLoadA = tk.Label(self.centerFrame)
       self.ModAstLoadA["text"] = "Warm-Up Load(kp): "
       self.ModAstLoadA.grid(row=2, column=0)

       self.ModAstLoadAText = tk.Text(self.centerFrame)
       self.ModAstLoadAText["height"] = 1
       self.ModAstLoadAText["width"] = 5
       self.ModAstLoadAText.bind("<Tab>", self.focus_next_window)
       self.ModAstLoadAText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstLoadAText.grid(row=2, column =1)

       self.ModAstLoadB = tk.Label(self.centerFrame)
       self.ModAstLoadB["text"] = "Work Load(kp): "
       self.ModAstLoadB.grid(row=3, column=0)

       self.ModAstLoadBText = tk.Text(self.centerFrame)
       self.ModAstLoadBText["height"] = 1
       self.ModAstLoadBText["width"] = 5
       self.ModAstLoadBText.bind("<Tab>", self.focus_next_window)
       self.ModAstLoadBText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstLoadBText.grid(row=3, column=1)

       self.ModAstHR = tk.Label(self.centerFrame)
       self.ModAstHR["text"] = "Average HR(bpm): "
       self.ModAstHR.grid(row=3, column=2)

       self.ModAstHRText = tk.Text(self.centerFrame)
       self.ModAstHRText["height"] = 1
       self.ModAstHRText["width"] = 5
       self.ModAstHRText.bind("<Tab>", self.focus_next_window)
       self.ModAstHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstHRText.grid(row=3, column=3)

       self.ModAstCapacity = tk.Label(self.centerFrame)
       self.ModAstCapacity["text"] = "Est. VO2max(kg/ml/min): "
       self.ModAstCapacity.grid(row=4, column=0)

       self.ModAstCapacityText = tk.Text(self.centerFrame)
       self.ModAstCapacityText["height"] = 1
       self.ModAstCapacityText["width"] = 5
       self.ModAstCapacityText.bind("<Tab>", self.focus_next_window)
       self.ModAstCapacityText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstCapacityText.grid(row=4, column=1)

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

       self.ModAstLoadAText.delete(1.0, tk.END)
       self.ModAstLoadAText.insert(tk.END, person.modAstLoadA)

       self.ModAstLoadBText.delete(1.0, tk.END)
       self.ModAstLoadBText.insert(tk.END, person.modAstLoadB)

       self.ModAstHRText.delete(1.0, tk.END)
       self.ModAstHRText.insert(tk.END, person.modAstHR)

       self.ModAstCapacityText.delete(1.0, tk.END)
       self.ModAstCapacityText.insert(tk.END, person.modAstAerobic)

   def saveData(self, person):
       person.modAstLoadA = self.ModAstLoadAText.get(1.0, tk.END).strip()
       person.modAstLoadB = self.ModAstLoadBText.get(1.0, tk.END).strip()
       person.modAstHR = self.ModAstHRText.get(1.0, tk.END).strip()
       person.modAstAerobic = self.ModAstCapacityText.get(1.0, tk.END).strip()
