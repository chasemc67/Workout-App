import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class SLstance(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.SLOpenLeftText.get(1.0, tk.END).strip())
          self.SLOpenLeftText.config(bg="white")
       except:
          self.SLOpenLeftText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SLOpenRightText.get(1.0, tk.END).strip())
          self.SLOpenRightText.config(bg="white")
       except:
          self.SLOpenRightText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SLCloseLeftText.get(1.0, tk.END).strip())
          self.SLCloseLeftText.config(bg="white")
       except:
          self.SLCloseLeftText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SLCloseRightText.get(1.0, tk.END).strip())
          self.SLCloseRightText.config(bg="white")
       except:
          self.SLCloseRightText.config(bg="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SLStance = tk.Label(self)
       self.SLStance["text"] = "Single Leg Stance Test"
       self.SLStance.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.SLOpenLeft = tk.Label(self.centerFrame)
       self.SLOpenLeft["text"] = "Eyes Open Left(sec.): "
       self.SLOpenLeft.grid(row=1, column=0)

       self.SLOpenLeftText = tk.Text(self.centerFrame)
       self.SLOpenLeftText["height"] = 1
       self.SLOpenLeftText["width"] = 5
       self.SLOpenLeftText.bind("<Tab>", self.focus_next_window)
       self.SLOpenLeftText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLOpenLeftText.grid(row=1, column=1)

       self.SLOpenRight = tk.Label(self.centerFrame)
       self.SLOpenRight["text"] = "Eyes Open Right(sec.): "
       self.SLOpenRight.grid(row=1, column=2)

       self.SLOpenRightText = tk.Text(self.centerFrame)
       self.SLOpenRightText["height"] = 1
       self.SLOpenRightText["width"] = 5
       self.SLOpenRightText.bind("<Tab>", self.focus_next_window)
       self.SLOpenRightText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLOpenRightText.grid(row=1, column=3)

       self.SLCloseLeft = tk.Label(self.centerFrame)
       self.SLCloseLeft["text"] = "Eyes Closed Left(sec.): "
       self.SLCloseLeft.grid(row=2, column=0)

       self.SLCloseLeftText = tk.Text(self.centerFrame)
       self.SLCloseLeftText["height"] = 1
       self.SLCloseLeftText["width"] = 5
       self.SLCloseLeftText.bind("<Tab>", self.focus_next_window)
       self.SLCloseLeftText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLCloseLeftText.grid(row=2, column=1)

       self.SLCloseRight = tk.Label(self.centerFrame)
       self.SLCloseRight["text"] = "Eyes Closed Right(sec.): "
       self.SLCloseRight.grid(row=2, column=2)

       self.SLCloseRightText = tk.Text(self.centerFrame)
       self.SLCloseRightText["height"] = 1
       self.SLCloseRightText["width"] = 5
       self.SLCloseRightText.bind("<Tab>", self.focus_next_window)
       self.SLCloseRightText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLCloseRightText.grid(row=2, column=3)

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

       self.SLOpenLeftText.delete(1.0, tk.END)
       self.SLOpenLeftText.insert(tk.END, person.SLOpenLeft)

       self.SLOpenRightText.delete(1.0, tk.END)
       self.SLOpenRightText.insert(tk.END, person.SLOpenRight)

       self.SLCloseLeftText.delete(1.0, tk.END)
       self.SLCloseLeftText.insert(tk.END, person.SLCloseLeft)

       self.SLCloseRightText.delete(1.0, tk.END)
       self.SLCloseRightText.insert(tk.END, person.SLCloseRight)

   def saveData(self, person):
       person.SLOpenLeft = self.SLOpenLeftText.get(1.0, tk.END).strip()
       person.SLOpenRight = self.SLOpenRightText.get(1.0, tk.END).strip()
       person.SLCloseLeft = self.SLCloseLeftText.get(1.0, tk.END).strip()
       person.SLCloseRight = self.SLCloseRightText.get(1.0, tk.END).strip()
