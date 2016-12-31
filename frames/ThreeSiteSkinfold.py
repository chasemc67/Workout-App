import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class ThreeSiteSkinfold(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ThreeSiteMaleCalc = tk.Label(self)
       self.ThreeSiteMaleCalc["text"] = "3-Site Skinfold (Male)"
       self.ThreeSiteMaleCalc.grid(row=2, column=0)

       self.ThreeSiteMaleChest = tk.Label(self)
       self.ThreeSiteMaleChest["text"] = "Chest: "
       self.ThreeSiteMaleChest.grid(row=2, column=1)

       self.ThreeSiteMaleChestInput = tk.Text(self)
       self.ThreeSiteMaleChestInput["height"] = 1
       self.ThreeSiteMaleChestInput["width"] = 5
       self.ThreeSiteMaleChestInput.grid(row=2, column=2)

       self.ThreeSiteMaleAb = tk.Label(self)
       self.ThreeSiteMaleAb["text"] = "Abdomen: "
       self.ThreeSiteMaleAb.grid(row=2, column=3)

       self.ThreeSiteMaleAbInput = tk.Text(self)
       self.ThreeSiteMaleAbInput["height"] = 1
       self.ThreeSiteMaleAbInput["width"] = 5
       self.ThreeSiteMaleAbInput.grid(row=2, column=4)

       self.ThreeSiteMaleThigh = tk.Label(self)
       self.ThreeSiteMaleThigh["text"] = "Thigh: "
       self.ThreeSiteMaleThigh.grid(row=2, column=5)

       self.ThreeSiteMaleChestThigh = tk.Text(self)
       self.ThreeSiteMaleChestThigh["height"] = 1
       self.ThreeSiteMaleChestThigh["width"] = 5
       self.ThreeSiteMaleChestThigh.grid(row=2, column=6)

       self.ThreeSiteFemaleCalc = tk.Label(self)
       self.ThreeSiteFemaleCalc["text"] = "3-Site Skinfold (Female)"
       self.ThreeSiteFemaleCalc.grid(row=3, column=0)

       self.ThreeSiteFemaleSupra = tk.Label(self)
       self.ThreeSiteFemaleSupra["text"] = "Suprailiac: "
       self.ThreeSiteFemaleSupra.grid(row=3, column=1)

       self.ThreeSiteFemaleSupra = tk.Text(self)
       self.ThreeSiteFemaleSupra["height"] = 1
       self.ThreeSiteFemaleSupra["width"] = 5
       self.ThreeSiteFemaleSupra.grid(row=3, column=2)

       self.ThreeSiteFemaleTricep = tk.Label(self)
       self.ThreeSiteFemaleTricep["text"] = "Tricep: "
       self.ThreeSiteFemaleTricep.grid(row=3, column=3)

       self.ThreeSiteFemaleTricep = tk.Text(self)
       self.ThreeSiteFemaleTricep["height"] = 1
       self.ThreeSiteFemaleTricep["width"] = 5
       self.ThreeSiteFemaleTricep.grid(row=3, column=4)

       self.ThreeSiteFemaleThigh = tk.Label(self)
       self.ThreeSiteFemaleThigh["text"] = "Thigh: "
       self.ThreeSiteFemaleThigh.grid(row=3, column=5)

       self.ThreeSiteFemaleThigh = tk.Text(self)
       self.ThreeSiteFemaleThigh["height"] = 1
       self.ThreeSiteFemaleThigh["width"] = 5
       self.ThreeSiteFemaleThigh.grid(row=3, column=6)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)