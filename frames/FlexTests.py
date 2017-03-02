import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class FlexTests(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")
       
   def validateInput(self):
       validationSuccess = True
       try:
          float(self.SitReachDistText.get(1.0, tk.END).strip())
          self.SitReachDistText.config(highlightbackground="white")
       except:
          self.SitReachDistText.config(highlightbackground="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SitReach = tk.Label(self)
       self.SitReach["text"] = "Sit & Reach"
       self.SitReach.grid(row=0, column=0)

       self.SitReachDist = tk.Label(self)
       self.SitReachDist["text"] = "Max Distance (cm): "
       self.SitReachDist.grid(row=1, column=0)

       self.SitReachDistText = tk.Text(self)
       self.SitReachDistText["height"] = 1
       self.SitReachDistText["width"] = 5
       self.SitReachDistText.bind("<Tab>", self.focus_next_window)
       self.SitReachDistText.bind("<Shift-Tab>", self.focus_last_window)
       self.SitReachDistText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.SitReachDistText.delete(1.0, tk.END)
       self.SitReachDistText.insert(tk.END, person.sitReachDist)

   def saveData(self, person):
       person.sitReachDist = self.SitReachDistText.get(1.0, tk.END).strip()
