import tkinter as tk
import parser.final_parser as fp
from shells import shell
from file_systemizer import file_systemizer as fsys
from list_creature import create_list
import os
import subprocess
class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.function_dict = {
            'graph': self.graph,
            'showme': self.showme,
            'list': self.create_list,
            'peek': self.peek,
            'connect': self.connect,
            'check' : self.check
        }
		
		self.file = None
		self.sh = shell.Shell()
		self.sh.grid()
		self.sh.ent_widget.bind('<Return>', self.bind_ent_widget_func)
		
		
	def bind_ent_widget_func(self, event):
		if self.sh.entry_var.get():
			self.sh.big_box.delete('1.0', tk.END)
#			self.fs = fsys.FileSystemizer(self.sh.entry_var.get())
		# command history list
		command = self.sh.entry_var.get()
		self.sh.command_history_list.append(command)
		# sp = subprocess.check_output(self.entry_var.get(), shell=True)

		# parsing text based commands and calling functions from entrybox widget
		
		self.func_list = list(filter(lambda func: func in self.function_dict, self.sh.entry_var.get().split()))
#		self.par = Parser(self.sh.entry_var.get())
#		self.filt_fun_list = self.par.func_list

		for item in self.func_list:
			if item in self.function_dict:
				self.function_dict[item]()
		self.sh.entry_var.set('')
		
	def showme(self):
		
		file = self.fs.showme()
		self.sh.big_box.insert('1.0', file)
#		print(file)

	def connect(self):
		self.fs = fsys.FileSystemizer(self.sh.entry_var.get())
		self.fs.connect()

#		self.file = self.fs.master_file (i did change this lastnight)
			
		if not self.fs.master_file:	
			self.sh.big_box.insert('1.0', f'{self.sh.entry_var.get().split()[1:]} is not a file')
		else:
			self.sh.big_box.insert('1.0', f'You are connected to {self.fs.master_file.parts[-1]}')
		
		
#		print(self.file)
	def check(self):
		if 'file' in self.sh.entry_var.get():
			self.sh.big_box.insert('1.0', self.fs.master_file.name)
		elif 'dir' in self.sh.entry_var.get():
			self.sh.big_box.insert('1.0', self.fs.master_file.parts[-2])
	def graph(self):
		print('hello')
			
	def create_list(self):
		lc = create_list.ListCreator(entry_var=self.sh.entry_var.get(),
									 file=self.fs.master_file)
#		lc.creatin_da_list()
#		print(lc.file)
		return_data = lc.creatin_da_list()
		for data in return_data[::-1]:
			self.sh.big_box.insert('1.0', str(data) + '\n')
		
	 	
		
			
	def peek(self):
		subprocess.run(['gedit', '{}'.format(self.fs.master_file)])
			
	def change_file(self):
		pass

if __name__ == '__main__':
	app = App()
	app.mainloop()
