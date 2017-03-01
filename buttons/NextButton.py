import tkinter as tk

class NextButton(tk.Button):

	def validateInput(self, saveFunction, validateFunction):
		if not validateFunction() == False:
			self.controller.next_page(saveFunction)

	def __init__(self, parent=None, controller=None, saveFunction=None, validateFunction=None, **config):
		tk.Button.__init__(self, parent, config)
		self.controller = controller
		self["text"] = "Next"
		self["fg"] = "black"
		if validateFunction != None:
			self["command"] = lambda: self.validateInput(saveFunction, validateFunction)
		else:
			self["command"] = lambda: controller.next_page(saveFunction)