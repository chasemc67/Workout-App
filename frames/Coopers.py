import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class Coopers(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.CooperDistText.get(1.0, tk.END).strip())
          self.CooperDistText.config(bg="white")
       except:
          self.CooperDistText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Cooper = tk.Label(self)
       self.Cooper["text"] = "Coopers Run"
       self.Cooper.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.CooperDist = tk.Label(self.centerFrame)
       self.CooperDist["text"] = "Distance(miles): "
       self.CooperDist.grid(row=1, column=0)

       self.CooperDistText = tk.Text(self.centerFrame)
       self.CooperDistText["height"] = 1
       self.CooperDistText["width"] = 5
       self.CooperDistText.bind("<Tab>", self.focus_next_window)
       self.CooperDistText.bind("<Shift-Tab>", self.focus_last_window)
       self.CooperDistText.grid(row=1, column=1)

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
      self.CooperDistText.delete(1.0, tk.END)
      self.CooperDistText.insert(tk.END, person.cooperDist)

   def saveData(self, person):
      person.cooperDist = self.CooperDistText.get(1.0, tk.END).strip()
