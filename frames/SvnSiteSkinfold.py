import tkinter as tk

class SvnSiteSkinfold(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SvnSiteSkFold = tk.Label(self)
       self.SvnSiteSkFold["text"] = "7-Site Skin Folds"
       self.SvnSiteSkFold.grid(row=0, column=0)

       self.SvnSiteChest = tk.Label(self)
       self.SvnSiteChest["text"] = "Chest: "
       self.SvnSiteChest.grid(row=1, column=0)

       self.SvnSiteChest = tk.Text(self)
       self.SvnSiteChest["height"] = 1
       self.SvnSiteChest["width"] = 5
       self.SvnSiteChest.grid(row=1, column=1)

       self.SvnSiteMidAx = tk.Label(self)
       self.SvnSiteMidAx["text"] = "Mid-Axillary: "
       self.SvnSiteMidAx.grid(row=1, column=2)

       self.SvnSiteMidAx = tk.Text(self)
       self.SvnSiteMidAx["height"] = 1
       self.SvnSiteMidAx["width"] = 5
       self.SvnSiteMidAx.grid(row=1, column=3)

       self.SvnSiteTri = tk.Label(self)
       self.SvnSiteTri["text"] = "Triceps: "
       self.SvnSiteTri.grid(row=1, column=4)

       self.SvnSiteTri = tk.Text(self)
       self.SvnSiteTri["height"] = 1
       self.SvnSiteTri["width"] = 5
       self.SvnSiteTri.grid(row=1, column=5)

       self.SvnSiteScap = tk.Label(self)
       self.SvnSiteScap["text"] = "Subscapular: "
       self.SvnSiteScap.grid(row=1, column=6)

       self.SvnSiteScap = tk.Text(self)
       self.SvnSiteScap["height"] = 1
       self.SvnSiteScap["width"] = 5
       self.SvnSiteScap.grid(row=1, column=7)

       self.SvnSiteSupra = tk.Label(self)
       self.SvnSiteSupra["text"] = "Suprailiac: "
       self.SvnSiteSupra.grid(row=1, column=8)

       self.SvnSiteSupra = tk.Text(self)
       self.SvnSiteSupra["height"] = 1
       self.SvnSiteSupra["width"] = 5
       self.SvnSiteSupra.grid(row=1, column=9)

       self.SvnSiteAb = tk.Label(self)
       self.SvnSiteAb["text"] = "Abdomen: "
       self.SvnSiteAb.grid(row=1, column=10)

       self.SvnSiteAb = tk.Text(self)
       self.SvnSiteAb["height"] = 1
       self.SvnSiteAb["width"] = 5
       self.SvnSiteAb.grid(row=1, column=11)

       self.SvnSiteThigh = tk.Label(self)
       self.SvnSiteThigh["text"] = "Thigh: "
       self.SvnSiteThigh.grid(row=1, column=12)

       self.SvnSiteThigh = tk.Text(self)
       self.SvnSiteThigh["height"] = 1
       self.SvnSiteThigh["width"] = 5
       self.SvnSiteThigh.grid(row=1, column=13)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=2, column=2)