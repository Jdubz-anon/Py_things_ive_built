import os
import pathlib
import subprocess
# pass entry var
class FileSystemizer:
	def __init__(self, inputs):
		self.master_path = '/media/'
		#comes from entry_var.get()
		self.user_filename = inputs.split()
		self.master_file = None
		count = 0
	def connect(self):
		for dir_path,dir_name,file_name in os.walk(self.master_path, topdown=False):
				for files in file_name:
					if files == self.user_filename[1]:
						self.master_file = pathlib.PurePath(dir_path,self.user_filename[1])
			

	def showme(self):
		return subprocess.check_output(['find', '/media', '-type', 'd', '-name', '{}'.format(self.user_filename[1]), '-exec', 'ls', '-l', '{}', ';'])
		
		
		
		
#fs = FileSystemizer('connect state_crime.csv')
#fs.connect()
#print(fs.master_file)

