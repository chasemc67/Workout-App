import tkinter as tk 

class PlaceholderTextBox(tk.Text):

	def onFocusIn(self, event):
		if self.get(1.0, tk.END).strip() == self.placeholder.strip():
			self.delete(1.0, tk.END) 

	def onFocusOut(self, event):
		if self.get(1.0, tk.END).strip() == "":
			self.delete(1.0, tk.END)
			self.insert(tk.END, self.placeholder)

	def __init__(self, parent=None, controller=None, placeholder=None, **config):
		tk.Text.__init__(self,parent, config)
		self.placeholder = placeholder
		self.delete(1.0, tk.END)
		self.insert(tk.END, self.placeholder)
		self.bind('<FocusIn>', self.onFocusIn)
		self.bind('<FocusOut>', self.onFocusOut)