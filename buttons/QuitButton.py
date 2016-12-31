import tkinter as tk

class QuitButton(tk.Button):
	def __init__(self, parent=None, controller=None, **config):
		tk.Button.__init__(self,parent, config)
		self["text"] = "Quit"
		self["fg"] = "black"
		self["command"] = lambda: controller.show_frame("MainPage")
