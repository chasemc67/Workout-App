import tkinter as tk

class NextButton(tk.Button):
	def __init__(self, parent=None, controller=None, **config):
		tk.Button.__init__(self, parent, config)
		self["text"] = "Next"
		self["fg"] = "black"
		self["command"] = lambda: controller.next_page()