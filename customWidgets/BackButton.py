import tkinter as tk

class BackButton(tk.Button):
	def __init__(self, parent=None, controller=None, saveFunction=None, **config):
		tk.Button.__init__(self,parent, config)
		self["text"] = "Back"
		self["fg"] = "black"
		self["command"] = lambda: controller.prev_page(saveFunction)
