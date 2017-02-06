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

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ThreeSiteMaleCalc = tk.Label(self)
       self.ThreeSiteMaleCalc["text"] = "3-Site Skinfold (Male)"
       self.ThreeSiteMaleCalc.grid(row=2, column=0)

       self.ThreeSiteMaleChest = tk.Label(self)
       self.ThreeSiteMaleChest["text"] = "Chest(mm): "
       self.ThreeSiteMaleChest.grid(row=2, column=1)

       self.ThreeSiteMaleChestText = tk.Text(self)
       self.ThreeSiteMaleChestText["height"] = 1
       self.ThreeSiteMaleChestText["width"] = 5
       self.ThreeSiteMaleChestText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteMaleChestText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteMaleChestText.grid(row=2, column=2)

       self.ThreeSiteMaleAb = tk.Label(self)
       self.ThreeSiteMaleAb["text"] = "Abdomen(mm): "
       self.ThreeSiteMaleAb.grid(row=2, column=3)

       self.ThreeSiteMaleAbText = tk.Text(self)
       self.ThreeSiteMaleAbText["height"] = 1
       self.ThreeSiteMaleAbText["width"] = 5
       self.ThreeSiteMaleAbText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteMaleAbText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteMaleAbText.grid(row=2, column=4)

       self.ThreeSiteMaleThigh = tk.Label(self)
       self.ThreeSiteMaleThigh["text"] = "Thigh(mm): "
       self.ThreeSiteMaleThigh.grid(row=2, column=5)

       self.ThreeSiteMaleThighText = tk.Text(self)
       self.ThreeSiteMaleThighText["height"] = 1
       self.ThreeSiteMaleThighText["width"] = 5
       self.ThreeSiteMaleThighText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteMaleThighText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteMaleThighText.grid(row=2, column=6)

       self.ThreeSiteFemaleCalc = tk.Label(self)
       self.ThreeSiteFemaleCalc["text"] = "3-Site Skinfold (Female)"
       self.ThreeSiteFemaleCalc.grid(row=3, column=0)

       self.ThreeSiteFemaleSupra = tk.Label(self)
       self.ThreeSiteFemaleSupra["text"] = "Suprailiac(mm): "
       self.ThreeSiteFemaleSupra.grid(row=3, column=1)

       self.ThreeSiteFemaleSupraText = tk.Text(self)
       self.ThreeSiteFemaleSupraText["height"] = 1
       self.ThreeSiteFemaleSupraText["width"] = 5
       self.ThreeSiteFemaleSupraText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteFemaleSupraText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteFemaleSupraText.grid(row=3, column=2)

       self.ThreeSiteFemaleTricep = tk.Label(self)
       self.ThreeSiteFemaleTricep["text"] = "Tricep(mm): "
       self.ThreeSiteFemaleTricep.grid(row=3, column=3)

       self.ThreeSiteFemaleTricepText = tk.Text(self)
       self.ThreeSiteFemaleTricepText["height"] = 1
       self.ThreeSiteFemaleTricepText["width"] = 5
       self.ThreeSiteFemaleTricepText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteFemaleTricepText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteFemaleTricepText.grid(row=3, column=4)

       self.ThreeSiteFemaleThigh = tk.Label(self)
       self.ThreeSiteFemaleThigh["text"] = "Thigh(mm): "
       self.ThreeSiteFemaleThigh.grid(row=3, column=5)

       self.ThreeSiteFemaleThighText = tk.Text(self)
       self.ThreeSiteFemaleThighText["height"] = 1
       self.ThreeSiteFemaleThighText["width"] = 5
       self.ThreeSiteFemaleThighText.bind("<Tab>", self.focus_next_window)
       self.ThreeSiteFemaleThighText.bind("<Shift-Tab>", self.focus_last_window)
       self.ThreeSiteFemaleThighText.grid(row=3, column=6)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)

   def loadData(self, person):

       self.ThreeSiteMaleChestText.delete(1.0, tk.END)
       self.ThreeSiteMaleChestText.insert(tk.END, person.threeSiteMaleChest)

       self.ThreeSiteMaleAbText.delete(1.0, tk.END)
       self.ThreeSiteMaleAbText.insert(tk.END, person.threeSiteMaleAb)

       self.ThreeSiteMaleThighText.delete(1.0, tk.END)
       self.ThreeSiteMaleThighText.insert(tk.END, person.threeSiteMaleThigh)

       self.ThreeSiteFemaleSupraText.delete(1.0, tk.END)
       self.ThreeSiteFemaleSupraText.insert(tk.END, person.threeSiteFemaleSupra)

       self.ThreeSiteFemaleTricepText.delete(1.0, tk.END)
       self.ThreeSiteFemaleTricepText.insert(tk.END, person.threeSiteFemaleTricep)

       self.ThreeSiteFemaleThighText.delete(1.0, tk.END)
       self.ThreeSiteFemaleThighText.insert(tk.END, person.threeSiteFemaleThigh)

   def saveData(self, person):
       person.threeSiteMaleChest = self.ThreeSiteMaleChestText.get(1.0, tk.END)
       person.threeSiteMaleAb = self.ThreeSiteMaleAbText.get(1.0, tk.END)
       person.threeSiteMaleThigh = self.ThreeSiteMaleThighText.get(1.0, tk.END)
       person.threeSiteFemaleSupra = self.ThreeSiteFemaleSupraText.get(1.0, tk.END)
       person.threeSiteFemaleTricep = self.ThreeSiteFemaleTricepText.get(1.0, tk.END)
       person.threeSiteFemaleThigh = self.ThreeSiteFemaleThighText.get(1.0, tk.END)
