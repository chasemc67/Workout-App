import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class ModAst(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ModAst = tk.Label(self)
       self.ModAst["text"] = "Modified Astrand"
       self.ModAst.grid(row=1, column=0)

       self.ModAstLoadA = tk.Label(self)
       self.ModAstLoadA["text"] = "Warm-Up Load(kp): "
       self.ModAstLoadA.grid(row=2, column=0)

       self.ModAstLoadAText = tk.Text(self)
       self.ModAstLoadAText["height"] = 1
       self.ModAstLoadAText["width"] = 5
       self.ModAstLoadAText.bind("<Tab>", self.focus_next_window)
       self.ModAstLoadAText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstLoadAText.grid(row=2, column =1)

       self.ModAstLoadB = tk.Label(self)
       self.ModAstLoadB["text"] = "Work Load(kp): "
       self.ModAstLoadB.grid(row=3, column=0)

       self.ModAstLoadBText = tk.Text(self)
       self.ModAstLoadBText["height"] = 1
       self.ModAstLoadBText["width"] = 5
       self.ModAstLoadBText.bind("<Tab>", self.focus_next_window)
       self.ModAstLoadBText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstLoadBText.grid(row=3, column=1)

       self.ModAstHR = tk.Label(self)
       self.ModAstHR["text"] = "Average HR(bpm): "
       self.ModAstHR.grid(row=3, column=2)

       self.ModAstHRText = tk.Text(self)
       self.ModAstHRText["height"] = 1
       self.ModAstHRText["width"] = 5
       self.ModAstHRText.bind("<Tab>", self.focus_next_window)
       self.ModAstHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstHRText.grid(row=3, column=3)

       self.ModAstCapacity = tk.Label(self)
       self.ModAstCapacity["text"] = "Est. VO2max(kg/ml/min): "
       self.ModAstCapacity.grid(row=4, column=0)

       self.ModAstCapacityText = tk.Text(self)
       self.ModAstCapacityText["height"] = 1
       self.ModAstCapacityText["width"] = 5
       self.ModAstCapacityText.bind("<Tab>", self.focus_next_window)
       self.ModAstCapacityText.bind("<Shift-Tab>", self.focus_last_window)
       self.ModAstCapacityText.grid(row=4, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=5, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=5, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=5, column=2)

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
