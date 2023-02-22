import tkinter as tk
import parser.final_parser as fp
from shells import shell
from file_systemizer import file_systemizer as fsys
from list_creature import create_list
import subprocess

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.columnconfigure(0,weight=1)
		self.rowconfigure(0,weight=1)
		self.function_dict = {
            'graph': self.graph,
            'showme': self.showme,
            'list': self.create_list,
            'peek': self.peek,
            'connect': self.connect,
            'check' : self.check
        }
		
		self.sh = shell.Shell()
		# added
		self.sh.columnconfigure(0,weight=1)
		self.sh.rowconfigure(0,weight=1)
		self.sh.grid(sticky='nsew',padx=20,pady=20)
		
		
		self.sh.ent_widget.bind('<Return>', self.bind_ent_widget_func)
		
		
	def bind_ent_widget_func(self, event):
		if self.sh.entry_var.get():
			self.sh.big_box.delete('1.0', tk.END)

		# command history list
		command = self.sh.entry_var.get()
		self.sh.command_history_list.append(command)

		# parsing text based commands and calling functions from entrybox widget
		
		self.func_list = list(filter(lambda func: func in self.function_dict, self.sh.entry_var.get().split()))
		if not self.func_list:
			self.sh.big_box.insert('1.0', 'Need to begin your Query with a command ')
		
		elif len(self.func_list) > 1:
			self.sh.big_box.insert('1.0', 'Too Many Functions, Try Again')
		
		else:
			for item in self.func_list:
				if item in self.function_dict:
					self.function_dict[item]()
		self.sh.entry_var.set('')
		
	def showme(self):
		self.fs = fsys.FileSystemizer(self.sh.entry_var.get())
		file = self.fs.showme()
		self.sh.big_box.insert('1.0', file)

	def connect(self):
		self.fs = fsys.FileSystemizer(self.sh.entry_var.get())
		self.fs.connect()
		
		if self.fs.master_file:
			self.sh.big_box.insert('1.0', f'You are connected to {self.fs.master_file.name}')
		else:
			self.sh.big_box.insert('1.0', f'Please enter a valid file name')
		
	def check(self):
		if self.fs.master_file:
			if 'file' in self.sh.entry_var.get(): 
				self.sh.big_box.insert('1.0', self.fs.master_file.name)
			elif 'dir' in self.sh.entry_var.get():
				self.sh.big_box.insert('1.0', self.fs.master_file.parts[-2])
		else:
			self.sh.big_box.insert('1.0', "Need to connect to a file!")
				
				
	def graph(self):
		print('hello')
			
	def create_list(self):
		try:	
			try:
				lc = create_list.ListCreator(entry_var=self.sh.entry_var.get(),
										 file_path=self.fs.master_file)
				try:
					for data in lc.creatin_da_list()[::-1]:
						self.sh.big_box.insert('1.0', (str(data) + '\n'))
				except TypeError:
					self.sh.big_box.insert('1.0', "No Matches")
			except AttributeError:
				self.sh.big_box.insert('1.0', "Need to connect to a file first!")
		except IndexError:
		 	self.sh.big_box.insert('1.0', 'Bad Syntax, Try again')
		
			
	def peek(self):
		try:
			subprocess.run(['gedit', '{}'.format(self.fs.master_file)])
		except AttributeError:
			self.sh.big_box.insert('1.0', 'Need to connect to a file first!')
	

if __name__ == '__main__':
	app = App()
	app.mainloop()
