import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class RMpredict(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RMPredict = tk.Label(self)
       self.RMPredict["text"] = "1 Rep Max.(Predicted)"
       self.RMPredict.grid(row=0, column=0)

       self.RMPredictEx = tk.Label(self)
       self.RMPredictEx["text"] = "Exercise: "
       self.RMPredictEx.grid(row=1, column=0)

       self.RMPredictEx = tk.Text(self)
       self.RMPredictEx["height"] = 1
       self.RMPredictEx["width"] = 5
       self.RMPredictEx.grid(row=1, column=1)

       self.RMPredictReps = tk.Label(self)
       self.RMPredictReps["text"] = "Reps: "
       self.RMPredictReps.grid(row=2, column=0)

       self.RMPredictReps = tk.Text(self)
       self.RMPredictReps["height"] = 1
       self.RMPredictReps["width"] = 5
       self.RMPredictReps.grid(row=2, column=1)

       self.RMPredictEst = tk.Label(self)
       self.RMPredictEst["text"] = "Estimated 1RM(kg): "
       self.RMPredictEst.grid(row=3, column=0)

       self.RMPredictEst = tk.Text(self)
       self.RMPredictEst["height"] = 1
       self.RMPredictEst["width"] = 5
       self.RMPredictEst.grid(row=3, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)