import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Coopers(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Cooper = tk.Label(self)
       self.Cooper["text"] = "Coopers Run"
       self.Cooper.grid(row=0, column=0)

       self.CooperDist = tk.Label(self)
       self.CooperDist["text"] = "Distance(miles): "
       self.CooperDist.grid(row=1, column=0)

       self.CooperDistText = tk.Text(self)
       self.CooperDistText["height"] = 1
       self.CooperDistText["width"] = 5
       self.CooperDistText.bind("<Tab>", self.focus_next_window)
       self.CooperDistText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):
      self.CooperDistText.delete(1.0, tk.END)
      self.CooperDistText.insert(tk.END, person.cooperDist)

   def saveData(self, person):
      person.cooperDist = self.CooperDistText.get(1.0, tk.END)
