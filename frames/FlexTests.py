import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

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
          self.SitReachDistText.config(bg="white")
       except:
          self.SitReachDistText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SitReach = tk.Label(self)
       self.SitReach["text"] = "Sit & Reach"
       self.SitReach.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.SitReachDist = tk.Label(self.centerFrame)
       self.SitReachDist["text"] = "Max Distance (cm): "
       self.SitReachDist.grid(row=1, column=0)

       self.SitReachDistText = tk.Text(self.centerFrame)
       self.SitReachDistText["height"] = 1
       self.SitReachDistText["width"] = 5
       self.SitReachDistText.bind("<Tab>", self.focus_next_window)
       self.SitReachDistText.bind("<Shift-Tab>", self.focus_last_window)
       self.SitReachDistText.grid(row=1, column=1)

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

       self.SitReachDistText.delete(1.0, tk.END)
       self.SitReachDistText.insert(tk.END, person.sitReachDist)

   def saveData(self, person):
       person.sitReachDist = self.SitReachDistText.get(1.0, tk.END).strip()
