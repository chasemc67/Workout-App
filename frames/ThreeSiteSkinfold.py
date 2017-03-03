import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

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
          self.ThreeSiteOneText.config(highlightbackground="white")
       except:
          self.ThreeSiteOneText.config(highlightbackground="red")
          validationSuccess = False

       try:
          float(self.ThreeSiteTwoText.get(1.0, tk.END).strip())
          self.ThreeSiteTwoText.config(highlightbackground="white")
       except:
          self.ThreeSiteTwoText.config(highlightbackground="red")
          validationSuccess = False

       try:
          float(self.ThreeSiteThreeText.get(1.0, tk.END).strip())
          self.ThreeSiteThreeText.config(highlightbackground="white")
       except:
          self.ThreeSiteThreeText.config(highlightbackground="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ThreeSiteCalc = tk.Label(self)
       self.ThreeSiteCalc.grid(row=2, column=0)

       self.ThreeSiteOne = tk.Label(self)
       self.ThreeSiteOne.grid(row=2, column=1)

       self.ThreeSiteOneText = tk.Text(self)
       self.ThreeSiteOneText["height"] = 1
       self.ThreeSiteOneText["width"] = 5
       self.ThreeSiteOneText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteOneText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteOneText.grid(row=2, column=2)

       self.ThreeSiteTwo = tk.Label(self)
       self.ThreeSiteTwo.grid(row=2, column=3)

       self.ThreeSiteTwoText = tk.Text(self)
       self.ThreeSiteTwoText["height"] = 1
       self.ThreeSiteTwoText["width"] = 5
       self.ThreeSiteTwoText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteTwoText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteTwoText.grid(row=2, column=4)

       self.ThreeSiteThree = tk.Label(self)
       self.ThreeSiteThree.grid(row=2, column=5)

       self.ThreeSiteThreeText = tk.Text(self)
       self.ThreeSiteThreeText["height"] = 1
       self.ThreeSiteThreeText["width"] = 5
       self.ThreeSiteThreeText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteThreeText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteThreeText.grid(row=2, column=6)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)

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

