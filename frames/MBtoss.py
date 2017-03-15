import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class MBtoss(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.SeatMBDistText.get(1.0, tk.END).strip())
          self.SeatMBDistText.config(bg="white")
       except:
          self.SeatMBDistText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.centerFrame = tk.Frame(self)

       self.SeatMB = tk.Label(self.centerFrame)
       self.SeatMB["text"] = "Seated Med. Ball Toss"
       self.SeatMB.grid(row=0, column=0)

       self.SeatMBDist = tk.Label(self.centerFrame)
       self.SeatMBDist["text"] = "Max. Distance(cm): "
       self.SeatMBDist.grid(row=1, column=0)

       self.SeatMBDistText = tk.Text(self.centerFrame)
       self.SeatMBDistText["height"] = 1
       self.SeatMBDistText["width"] = 5
       self.SeatMBDistText.bind("<Tab>", self.focus_next_window)
       self.SeatMBDistText.bind("<Shift-Tab>", self.focus_last_window)
       self.SeatMBDistText.grid(row=1, column=1)

       self.centerFrame.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

   def loadData(self, person):

       self.SeatMBDistText.delete(1.0, tk.END)
       self.SeatMBDistText.insert(tk.END, person.seatMBDist)

   def saveData(self, person):
       person.seatMBDist = self.SeatMBDistText.get(1.0, tk.END).strip()
