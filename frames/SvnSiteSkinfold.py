import tkinter as tk

from customWidgets.NextButton import NextButton
from customWidgets.BackButton import BackButton
from customWidgets.QuitButton import QuitButton

class SvnSiteSkinfold(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")


   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def validateInput(self):
       validationSuccess = True
       try:
          float(self.SvnSiteChestText.get(1.0, tk.END).strip())
          self.SvnSiteChestText.config(bg="white")
       except:
          self.SvnSiteChestText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteMidAxText.get(1.0, tk.END).strip())
          self.SvnSiteMidAxText.config(bg="white")
       except:
          self.SvnSiteMidAxText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteTriText.get(1.0, tk.END).strip())
          self.SvnSiteTriText.config(bg="white")
       except:
          self.SvnSiteTriText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteScapText.get(1.0, tk.END).strip())
          self.SvnSiteScapText.config(bg="white")
       except:
          self.SvnSiteScapText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteSupraText.get(1.0, tk.END).strip())
          self.SvnSiteSupraText.config(bg="white")
       except:
          self.SvnSiteSupraText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteAbText.get(1.0, tk.END).strip())
          self.SvnSiteAbText.config(bg="white")
       except:
          self.SvnSiteAbText.config(bg="red")
          validationSuccess = False

       try:
          float(self.SvnSiteThighText.get(1.0, tk.END).strip())
          self.SvnSiteThighText.config(bg="white")
       except:
          self.SvnSiteThighText.config(bg="red")
          validationSuccess = False
          
       return validationSuccess

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SvnSiteSkFold = tk.Label(self)
       self.SvnSiteSkFold["text"] = "7-Site Skin Folds"
       self.SvnSiteSkFold.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.centerFrame = tk.Frame(self)

       self.SvnSiteChest = tk.Label(self.centerFrame)
       self.SvnSiteChest["text"] = "Chest(mm): "
       self.SvnSiteChest.grid(row=1, column=0)

       self.SvnSiteChestText = tk.Text(self.centerFrame)
       self.SvnSiteChestText["height"] = 1
       self.SvnSiteChestText["width"] = 5
       self.SvnSiteChestText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteChestText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteChestText.grid(row=1, column=1)

       self.SvnSiteMidAx = tk.Label(self.centerFrame)
       self.SvnSiteMidAx["text"] = "Mid-Axillary(mm): "
       self.SvnSiteMidAx.grid(row=2, column=0)

       self.SvnSiteMidAxText = tk.Text(self.centerFrame)
       self.SvnSiteMidAxText["height"] = 1
       self.SvnSiteMidAxText["width"] = 5
       self.SvnSiteMidAxText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteMidAxText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteMidAxText.grid(row=2, column=1)

       self.SvnSiteTri = tk.Label(self.centerFrame)
       self.SvnSiteTri["text"] = "Triceps(mm): "
       self.SvnSiteTri.grid(row=3, column=0)

       self.SvnSiteTriText = tk.Text(self.centerFrame)
       self.SvnSiteTriText["height"] = 1
       self.SvnSiteTriText["width"] = 5
       self.SvnSiteTriText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteTriText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteTriText.grid(row=3, column=1)

       self.SvnSiteScap = tk.Label(self.centerFrame)
       self.SvnSiteScap["text"] = "Subscapular(mm): "
       self.SvnSiteScap.grid(row=4, column=0)

       self.SvnSiteScapText = tk.Text(self.centerFrame)
       self.SvnSiteScapText["height"] = 1
       self.SvnSiteScapText["width"] = 5
       self.SvnSiteScapText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteScapText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteScapText.grid(row=4, column=1)

       self.SvnSiteSupra = tk.Label(self.centerFrame)
       self.SvnSiteSupra["text"] = "Suprailiac(mm): "
       self.SvnSiteSupra.grid(row=5, column=0)

       self.SvnSiteSupraText = tk.Text(self.centerFrame)
       self.SvnSiteSupraText["height"] = 1
       self.SvnSiteSupraText["width"] = 5
       self.SvnSiteSupraText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteSupraText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteSupraText.grid(row=5, column=1)

       self.SvnSiteAb = tk.Label(self.centerFrame)
       self.SvnSiteAb["text"] = "Abdomen(mm): "
       self.SvnSiteAb.grid(row=6, column=0)

       self.SvnSiteAbText = tk.Text(self.centerFrame)
       self.SvnSiteAbText["height"] = 1
       self.SvnSiteAbText["width"] = 5
       self.SvnSiteAbText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteAbText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteAbText.grid(row=6, column=1)

       self.SvnSiteThigh = tk.Label(self.centerFrame)
       self.SvnSiteThigh["text"] = "Thigh(mm): "
       self.SvnSiteThigh.grid(row=7, column=0)

       self.SvnSiteThighText = tk.Text(self.centerFrame)
       self.SvnSiteThighText["height"] = 1
       self.SvnSiteThighText["width"] = 5
       self.SvnSiteThighText.bind("<Tab>", self.focus_next_window)
       self.SvnSiteThighText.bind("<Shift-Tab>", self.focus_last_window)
       self.SvnSiteThighText.grid(row=7, column=1)

       self.centerFrame.pack()

       spacer = tk.Label(self)
       spacer.pack()

       self.buttonFrame = tk.Frame(self)
       self.Next = NextButton(self.buttonFrame, controller, self.saveData, self.validateInput)
       self.Next.grid(row=0, column=0)

       self.Back = BackButton(self.buttonFrame, controller)
       self.Back.grid(row=0, column=1)

       self.Quit = QuitButton(self.buttonFrame, controller)
       self.Quit.grid(row=0, column=2)
       self.buttonFrame.pack()

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
       person.svnSiteChest = self.SvnSiteChestText.get(1.0, tk.END).strip()
       person.svnSiteMidAx = self.SvnSiteMidAxText.get(1.0, tk.END).strip()
       person.svnSiteTri = self.SvnSiteTriText.get(1.0, tk.END).strip()
       person.svnSiteScap = self.SvnSiteScapText.get(1.0, tk.END).strip()
       person.svnSiteSupra = self.SvnSiteSupraText.get(1.0, tk.END).strip()
       person.svnSiteAb = self.SvnSiteAbText.get(1.0, tk.END).strip()
       person.svnSiteThigh = self.SvnSiteThighText.get(1.0, tk.END).strip()
