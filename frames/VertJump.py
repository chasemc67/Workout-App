import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class VertJump(tk.Frame):
 
   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.VertJumpSRText.get(1.0, tk.END).strip())
          self.VertJumpSRText.config(bg="white")
       except:
          self.VertJumpSRText.config(bg="red")
          validationSuccess = False

       try:
          float(self.VertJumpBestText.get(1.0, tk.END).strip())
          self.VertJumpBestText.config(bg="white")
       except:
          self.VertJumpBestText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.VertJump = tk.Label(self)
       self.VertJump["text"] = "Vertical Jump"
       self.VertJump.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.VertJumpSR = tk.Label(self.centerFrame)
       self.VertJumpSR["text"] = "Standing Reach(ft.inch): "
       self.VertJumpSR.grid(row=1, column=0)

       self.VertJumpSRText = tk.Text(self.centerFrame)
       self.VertJumpSRText["height"] = 1
       self.VertJumpSRText["width"] = 5
       self.VertJumpSRText.bind("<Tab>", self.focus_next_window)
       self.VertJumpSRText.bind("<Shift-Tab>", self.focus_last_window)
       self.VertJumpSRText.grid(row=1, column=1)

       self.VertJumpBest = tk.Label(self.centerFrame)
       self.VertJumpBest["text"] = "Best Attempt(ft.inch): "
       self.VertJumpBest.grid(row=2, column=0)

       self.VertJumpBestText = tk.Text(self.centerFrame)
       self.VertJumpBestText["height"] = 1
       self.VertJumpBestText["width"] = 5
       self.VertJumpBestText.bind("<Tab>", self.focus_next_window)
       self.VertJumpBestText.bind("<Shift-Tab>", self.focus_last_window)
       self.VertJumpBestText.grid(row=2, column=1)

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

       self.VertJumpSRText.delete(1.0, tk.END)
       self.VertJumpSRText.insert(tk.END, person.vertJumpSR)

       self.VertJumpBestText.delete(1.0, tk.END)
       self.VertJumpBestText.insert(tk.END, person.vertJumpBest)

   def saveData(self, person):
       person.vertJumpSR = self.VertJumpSRText.get(1.0, tk.END).strip()
       person.vertJumpBest = self.VertJumpBestText.get(1.0, tk.END).strip()
