import os
import path
import subprocess
# pass entry var
class FileSystemizer:
	def __init__(self, user_filename):
		self.master_path = '/media/'
		#comes from entry_var.get()
		self.user_filename = user_filename
		self.master_file = None
		count = 0
	def connect(self):
		for dir_path,dir_name,file_name in os.walk(master_path, topdown=False):
				for files in file_name:
					if files == self.user_filename:
						self.master_file = pl.PurePath(dir_path,user_filename)
	def checking(self):
		check_file = os.fspath(master_file).split('/')
		print(check_file[-1])
		#check dir
		print(check_file[-2])

