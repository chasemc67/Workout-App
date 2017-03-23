import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class CurlUps(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.CurlUpNumText.get(1.0, tk.END).strip())
          self.CurlUpNumText.config(bg="white")
       except:
          self.CurlUpNumText.config(bg="red")
          validationSuccess = False
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.CurlUp = tk.Label(self)
       self.CurlUp["text"] = "10cm Curl Ups"
       self.CurlUp.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.CurlUpNum = tk.Label(self.centerFrame)
       self.CurlUpNum["text"] = "Number: "
       self.CurlUpNum.grid(row=1, column=0)

       self.CurlUpNumText = tk.Text(self.centerFrame)
       self.CurlUpNumText["height"] = 1
       self.CurlUpNumText["width"] = 5
       self.CurlUpNumText.bind("<Tab>", self.focus_next_window)
       self.CurlUpNumText.bind("<Shift-Tab>", self.focus_last_window)
       self.CurlUpNumText.grid(row=1, column=1)

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
       self.CurlUpNumText.delete(1.0, tk.END)
       self.CurlUpNumText.insert(tk.END, person.curlUpNum)

   def saveData(self, person):
       person.curlUpNum = self.CurlUpNumText.get(1.0, tk.END).strip()
