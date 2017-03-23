import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class WallSlide(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.WallSlideRateText.get(1.0, tk.END).strip())
          self.WallSlideRateText.config(bg="white")
       except:
          self.WallSlideRateText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSlide = tk.Label(self)
       self.WallSlide["text"] = "Wall Slide"
       self.WallSlide.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.WallSlideRate = tk.Label(self.centerFrame)
       self.WallSlideRate["text"] = "Rating(0-3): "
       self.WallSlideRate.grid(row=1, column=0)

       self.WallSlideRateText = tk.Text(self.centerFrame)
       self.WallSlideRateText["height"] = 1
       self.WallSlideRateText["width"] = 5
       self.WallSlideRateText.bind("<Tab>", self.focus_next_window)
       self.WallSlideRateText.bind("<Shift-Tab>", self.focus_last_window)
       self.WallSlideRateText.grid(row=1, column=1)

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

       self.WallSlideRateText.delete(1.0, tk.END)
       self.WallSlideRateText.insert(tk.END, person.wallSlideRate)

   def saveData(self, person):
       person.wallSlideRate = self.WallSlideRateText.get(1.0, tk.END).strip()
