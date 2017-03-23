import tkinter as tk
from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class Circumference(tk.Frame):

   def focus_next_window(self, event):
      event.widget.tk_focusNext().focus()
      return("break")
   
   def focus_last_window(self, event):
      event.widget.tk_focusPrev().focus()
      return("break")

   def validateInput(self):
      validationSuccess = True
      try:
            float(self.HipCircText.get(1.0, tk.END).strip())
            self.HipCircText.config(bg="white")
      except:
            self.HipCircText.config(bg="red")
            validationSuccess = False
      
      try:
            float(self.WaistCircText.get(1.0, tk.END).strip())
            self.WaistCircText.config(bg="white")
      except:
            self.WaistCircText.config(bg="red")
            validationSuccess = False
      
      try:
            float(self.ArmCircText.get(1.0, tk.END).strip())
            self.ArmCircText.config(bg="white")
      except:
            self.ArmCircText.config(bg="red")
            validationSuccess = False
      
      try:
            float(self.ThighCircText.get(1.0, tk.END).strip())
            self.ThighCircText.config(bg="white")
      except:
            self.ThighCircText.config(bg="red")
            validationSuccess = False
      
      try:
            float(self.ChestCircText.get(1.0, tk.END).strip())
            self.ChestCircText.config(bg="white")
      except:
            self.ChestCircText.config(bg="red")
            validationSuccess = False

      return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self,parent)
       self.controller = controller

       self.Circumference = tk.Label(self)
       self.Circumference["text"] = "Circumferences"
       self.Circumference.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.HipCirc = tk.Label(self.centerFrame)
       self.HipCirc["text"] = "Hip(cm): "
       self.HipCirc.grid(row=1, column=0)

       self.HipCircText = tk.Text(self.centerFrame)
       self.HipCircText["height"] = 1
       self.HipCircText["width"] = 5
       self.HipCircText.bind("<Tab>", self.focus_next_window)
       self.HipCircText.bind("<Shift-Tab>", self.focus_last_window)
       self.HipCircText.grid(row=1, column=1)

       self.WaistCirc = tk.Label(self.centerFrame)
       self.WaistCirc["text"] = "Waist(cm): "
       self.WaistCirc.grid(row=2, column=0)

       self.WaistCircText = tk.Text(self.centerFrame)
       self.WaistCircText["height"] = 1
       self.WaistCircText["width"] = 5
       self.WaistCircText.bind("<Tab>", self.focus_next_window)
       self.WaistCircText.bind("<Shift-Tab>", self.focus_last_window)
       self.WaistCircText.grid(row=2, column=1)

       self.ArmCirc = tk.Label(self.centerFrame)
       self.ArmCirc["text"] = "Arm(cm): "
       self.ArmCirc.grid(row=3, column=0)

       self.ArmCircText = tk.Text(self.centerFrame)
       self.ArmCircText["height"] = 1
       self.ArmCircText["width"] = 5
       self.ArmCircText.bind("<Tab>", self.focus_next_window)
       self.ArmCircText.bind("<Shift-Tab>", self.focus_last_window)
       self.ArmCircText.grid(row=3, column=1)

       self.ThighCirc = tk.Label(self.centerFrame)
       self.ThighCirc["text"] = "Thigh(cm): "
       self.ThighCirc.grid(row=4, column=0)

       self.ThighCircText = tk.Text(self.centerFrame)
       self.ThighCircText["height"] = 1
       self.ThighCircText["width"] = 5
       self.ThighCircText.bind("<Tab>", self.focus_next_window)
       self.ThighCircText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThighCircText.grid(row=4, column=1)

       self.ChestCirc = tk.Label(self.centerFrame)
       self.ChestCirc["text"] = "Chest(cm): "
       self.ChestCirc.grid(row=5, column=0)

       self.ChestCircText = tk.Text(self.centerFrame)
       self.ChestCircText["height"] = 1
       self.ChestCircText["width"] = 5
       self.ChestCircText.bind("<Tab>", self.focus_next_window)
       self.ChestCircText.bind("<Shift-Tab>", self.focus_last_window)
       self.ChestCircText.grid(row=5, column=1)

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
       self.HipCircText.delete(1.0, tk.END)
       self.HipCircText.insert(tk.END, person.hipCirc)

       self.WaistCircText.delete(1.0, tk.END)
       self.WaistCircText.insert(tk.END, person.waistCirc)

       self.ArmCircText.delete(1.0, tk.END)
       self.ArmCircText.insert(tk.END, person.armCirc)

       self.ThighCircText.delete(1.0, tk.END)
       self.ThighCircText.insert(tk.END, person.thighCirc)

       self.ChestCircText.delete(1.0, tk.END)
       self.ChestCircText.insert(tk.END, person.chestCirc)


   def saveData(self, person):
       person.hipCirc = self.HipCircText.get(1.0, tk.END).strip()
       person.waistCirc = self.WaistCircText.get(1.0, tk.END).strip()
       person.armCirc = self.ArmCircText.get(1.0, tk.END).strip()
       person.thighCirc = self.ThighCircText.get(1.0, tk.END).strip()
       person.chestCirc = self.ChestCircText.get(1.0, tk.END).strip()


