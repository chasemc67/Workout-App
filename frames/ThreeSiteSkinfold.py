import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class ThreeSiteSkinfold(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.ThreeSiteOneText.get(1.0, tk.END).strip())
          self.ThreeSiteOneText.config(bg="white")
       except:
          self.ThreeSiteOneText.config(bg="red")
          validationSuccess = False

       try:
          float(self.ThreeSiteTwoText.get(1.0, tk.END).strip())
          self.ThreeSiteTwoText.config(bg="white")
       except:
          self.ThreeSiteTwoText.config(bg="red")
          validationSuccess = False

       try:
          float(self.ThreeSiteThreeText.get(1.0, tk.END).strip())
          self.ThreeSiteThreeText.config(bg="white")
       except:
          self.ThreeSiteThreeText.config(bg="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ThreeSiteCalc = tk.Label(self)
       self.ThreeSiteCalc.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.ThreeSiteOne = tk.Label(self.centerFrame)
       self.ThreeSiteOne.grid(row=2, column=1)

       self.ThreeSiteOneText = tk.Text(self.centerFrame)
       self.ThreeSiteOneText["height"] = 1
       self.ThreeSiteOneText["width"] = 5
       self.ThreeSiteOneText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteOneText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteOneText.grid(row=2, column=2)

       self.ThreeSiteTwo = tk.Label(self.centerFrame)
       self.ThreeSiteTwo.grid(row=2, column=3)

       self.ThreeSiteTwoText = tk.Text(self.centerFrame)
       self.ThreeSiteTwoText["height"] = 1
       self.ThreeSiteTwoText["width"] = 5
       self.ThreeSiteTwoText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteTwoText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteTwoText.grid(row=2, column=4)

       self.ThreeSiteThree = tk.Label(self.centerFrame)
       self.ThreeSiteThree.grid(row=2, column=5)

       self.ThreeSiteThreeText = tk.Text(self.centerFrame)
       self.ThreeSiteThreeText["height"] = 1
       self.ThreeSiteThreeText["width"] = 5
       self.ThreeSiteThreeText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteThreeText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteThreeText.grid(row=2, column=6)

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

       if person.gender.lower() == "male":
        self.ThreeSiteCalc["text"] = "3-Site Skinfold (Male)"
        self.ThreeSiteOne["text"] = "Chest(mm): "
        self.ThreeSiteTwo["text"] = "Abdomen(mm): "
        self.ThreeSiteThree["text"] = "Thigh(mm): "

        self.ThreeSiteOneText.delete(1.0, tk.END)
        self.ThreeSiteOneText.insert(tk.END, person.threeSiteMaleChest)

        self.ThreeSiteTwoText.delete(1.0, tk.END)
        self.ThreeSiteTwoText.insert(tk.END, person.threeSiteMaleAb)

        self.ThreeSiteThreeText.delete(1.0, tk.END)
        self.ThreeSiteThreeText.insert(tk.END, person.threeSiteMaleThigh)
       
       else:
        self.ThreeSiteCalc["text"] = "3-Site Skinfold (Female)"
        self.ThreeSiteOne["text"] = "Suprailiac(mm): "
        self.ThreeSiteTwo["text"] = "Tricep(mm): "
        self.ThreeSiteThree["text"] = "Thigh(mm): "

        self.ThreeSiteOneText.delete(1.0, tk.END)
        self.ThreeSiteOneText.insert(tk.END, person.threeSiteFemaleSupra)

        self.ThreeSiteTwoText.delete(1.0, tk.END)
        self.ThreeSiteTwoText.insert(tk.END, person.threeSiteFemaleTricep)

        self.ThreeSiteThreeText.delete(1.0, tk.END)
        self.ThreeSiteThreeText.insert(tk.END, person.threeSiteFemaleThigh)
       

   def saveData(self, person):
       if person.gender.lower() == "male":
         person.threeSiteMaleChest = self.ThreeSiteOneText.get(1.0, tk.END).strip()
         person.threeSiteMaleAb = self.ThreeSiteTwoText.get(1.0, tk.END).strip()
         person.threeSiteMaleThigh = self.ThreeSiteThreeText.get(1.0, tk.END).strip()
       
       else:
         person.threeSiteFemaleSupra = self.ThreeSiteOneText.get(1.0, tk.END).strip()
         person.threeSiteFemaleTricep = self.ThreeSiteTwoText.get(1.0, tk.END).strip()
         person.threeSiteFemaleThigh = self.ThreeSiteThreeText.get(1.0, tk.END).strip()

