import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Ebelling(tk.Frame):
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.EbellingWUText.get(1.0, tk.END).strip())
          self.EbellingWUText.config(bg="white")
       except:
          self.EbellingWUText.config(bg="red")
          validationSuccess = False
       
       try:
          float(self.EbellingWorkText.get(1.0, tk.END).strip())
          self.EbellingWorkText.config(bg="white")
       except:
          self.EbellingWorkText.config(bg="red")
          validationSuccess = False

       try:
          float(self.EbellingHRText.get(1.0, tk.END).strip())
          self.EbellingHRText.config(bg="white")
       except:
          self.EbellingHRText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Ebelling = tk.Label(self)
       self.Ebelling["text"] = "Ebbeling Treadmill Test"
       self.Ebelling.grid(row=0, column=0)

       self.EbellingWU = tk.Label(self)
       self.EbellingWU["text"] = "Warm Up Speed"
       self.EbellingWU.grid(row=1, column=0)

       self.EbellingWUText = tk.Text(self)
       self.EbellingWUText["height"] = 1
       self.EbellingWUText["width"] = 5
       self.EbellingWUText.bind("<Tab>", self.focus_next_window)
       self.EbellingWUText.bind("<Shift-Tab>", self.focus_last_window)
       self.EbellingWUText.grid(row=1, column=1)

       self.EbellingWork = tk.Label(self)
       self.EbellingWork["text"] = "Workload Speed"
       self.EbellingWork.grid(row=2, column=0)

       self.EbellingWorkText = tk.Text(self)
       self.EbellingWorkText["height"] = 1
       self.EbellingWorkText["width"] = 5
       self.EbellingWorkText.bind("<Tab>", self.focus_next_window)
       self.EbellingWorkText.bind("<Shift-Tab>", self.focus_last_window)
       self.EbellingWorkText.grid(row=2, column=1)

       self.EbellingHR = tk.Label(self)
       self.EbellingHR["text"] = "Average HR"
       self.EbellingHR.grid(row=3, column=0)

       self.EbellingHRText = tk.Text(self)
       self.EbellingHRText["height"] = 1
       self.EbellingHRText["width"] = 5
       self.EbellingHRText.bind("<Tab>", self.focus_next_window)
       self.EbellingHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.EbellingHRText.grid(row=3, column=1)

       self.Next = NextButton(self, controller, self.saveData, self.validateInput)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)

   def loadData(self, person):

       self.EbellingWUText.delete(1.0, tk.END)
       self.EbellingWUText.insert(tk.END, person.ebbelingWU)

       self.EbellingWorkText.delete(1.0, tk.END)
       self.EbellingWorkText.insert(tk.END, person.ebbelingWork)

       self.EbellingHRText.delete(1.0, tk.END)
       self.EbellingHRText.insert(tk.END, person.ebbelingHR)

   def saveData(self, person):
       person.ebbelingWU = self.EbellingWUText.get(1.0, tk.END).strip()
       person.ebbelingWork = self.EbellingWorkText.get(1.0, tk.END).strip()
       person.ebbelingHR = self.EbellingHRText.get(1.0,tk.END).strip()
