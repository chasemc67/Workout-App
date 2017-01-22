import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class SvnSiteSkinfold(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SvnSiteSkFold = tk.Label(self)
       self.SvnSiteSkFold["text"] = "7-Site Skin Folds"
       self.SvnSiteSkFold.grid(row=0, column=0)

       self.SvnSiteChest = tk.Label(self)
       self.SvnSiteChest["text"] = "Chest(mm): "
       self.SvnSiteChest.grid(row=1, column=0)

       self.SvnSiteChestText = tk.Text(self)
       self.SvnSiteChestText["height"] = 1
       self.SvnSiteChestText["width"] = 5
       self.SvnSiteChestText.grid(row=1, column=1)

       self.SvnSiteMidAx = tk.Label(self)
       self.SvnSiteMidAx["text"] = "Mid-Axillary(mm): "
       self.SvnSiteMidAx.grid(row=1, column=2)

       self.SvnSiteMidAxText = tk.Text(self)
       self.SvnSiteMidAxText["height"] = 1
       self.SvnSiteMidAxText["width"] = 5
       self.SvnSiteMidAxText.grid(row=1, column=3)

       self.SvnSiteTri = tk.Label(self)
       self.SvnSiteTri["text"] = "Triceps(mm): "
       self.SvnSiteTri.grid(row=1, column=4)

       self.SvnSiteTriText = tk.Text(self)
       self.SvnSiteTriText["height"] = 1
       self.SvnSiteTriText["width"] = 5
       self.SvnSiteTriText.grid(row=1, column=5)

       self.SvnSiteScap = tk.Label(self)
       self.SvnSiteScap["text"] = "Subscapular(mm): "
       self.SvnSiteScap.grid(row=1, column=6)

       self.SvnSiteScapText = tk.Text(self)
       self.SvnSiteScapText["height"] = 1
       self.SvnSiteScapText["width"] = 5
       self.SvnSiteScapText.grid(row=1, column=7)

       self.SvnSiteSupra = tk.Label(self)
       self.SvnSiteSupra["text"] = "Suprailiac(mm): "
       self.SvnSiteSupra.grid(row=1, column=8)

       self.SvnSiteSupraText = tk.Text(self)
       self.SvnSiteSupraText["height"] = 1
       self.SvnSiteSupraText["width"] = 5
       self.SvnSiteSupraText.grid(row=1, column=9)

       self.SvnSiteAb = tk.Label(self)
       self.SvnSiteAb["text"] = "Abdomen(mm): "
       self.SvnSiteAb.grid(row=1, column=10)

       self.SvnSiteAbText = tk.Text(self)
       self.SvnSiteAbText["height"] = 1
       self.SvnSiteAbText["width"] = 5
       self.SvnSiteAbText.grid(row=1, column=11)

       self.SvnSiteThigh = tk.Label(self)
       self.SvnSiteThigh["text"] = "Thigh(mm): "
       self.SvnSiteThigh.grid(row=1, column=12)

       self.SvnSiteThighText = tk.Text(self)
       self.SvnSiteThighText["height"] = 1
       self.SvnSiteThighText["width"] = 5
       self.SvnSiteThighText.grid(row=1, column=13)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.SvnSiteChestText.delete(1.0, tk.END)
       self.SvnSiteChestText.insert(tk.END, person.svnSiteChest)

       self.SvnSiteMidAxText.delete(1.0, tk.END)
       self.SvnSiteMidAxText.insert(tk.END, person.svnSiteMidAx)

       self.SvnSiteTriText.delete(1.0, tk.END)
       self.SvnSiteTriText.insert(tk.END, person.svnSiteTri)

       self.SvnSiteScapText.delete(1.0, tk.END)
       self.SvnSiteScapText.insert(tk.END, person.svnSiteScap)

       self.SvnSiteSupraText.delete(1.0, tk.END)
       self.SvnSiteSupraText.insert(tk.END, person.svnSiteSupra)

       self.SvnSiteAbText.delete(1.0, tk.END)
       self.SvnSiteAbText.insert(tk.END, person.svnSiteAb)

       self.SvnSiteThighText.delete(1.0, tk.END)
       self.SvnSiteThighText.insert(tk.END, person.svnSiteThigh)

   def saveData(self, person):
       person.svnSiteChest = self.SvnSiteChestText.get(1.0, tk.END)
       person.svnSiteMidAx = self.SvnSiteMidAxText.get(1.0, tk.END)
       person.svnSiteTri = self.SvnSiteTriText.get(1.0, tk.END)
       person.svnSiteScap = self.SvnSiteScapText.get(1.0, tk.END)
       person.svnSiteSupra = self.SvnSiteSupraText.get(1.0, tk.END)
       person.svnSiteAb = self.SvnSiteAbText.get(1.0, tk.END)
       person.svnSiteThigh = self.SvnSiteThighText.get(1.0, tk.END)
