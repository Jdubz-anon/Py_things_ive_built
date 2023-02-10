import csv
#import sys #to run in gedit
#sys.path.append('/media/jdubzanon/SmallStorage/csv_app') #to run in gedit
from parser import parser3
#pass list_of_dicts and range dict and masterfile

ent = 'list state new-york&new-jersey date 1999-2020 category murder deathrate 1998'

class ListCreator(parser3.Parser3):
		def __init__(self, entry_var, file, *args):
			super().__init__(entry_var, *args)
			self.entry_var = entry_var.split()
			#master_file
			self.file = file
			self.csv_file = None
			
			
		def creatin_da_list(self):
			with open(self.file, mode='r') as csv_file:
				csv_file = csv.DictReader(csv_file)
				if self.split_input[-1] == 'cats':
					return csv_file.fieldnames
				elif self.split_input[-1] == 'catx':
					data = []
					count = 0
					for row in csv_file:
						count += 1
						if count == 2:
							for values in csv_file.fieldnames:
								data.append(f'{values} : {row[values]}')
					return data
				if len(self.entry_var) >= 3:
					self.parse()
					data = list()
					if self.rangedict:
						for row in csv_file:
							for dicts in self.rangedict:
								for key in dicts.keys(): #key for dict in rangedict
									for num in range(int(dicts[key][0]), int(dicts[key][1]) + 1):							
										for key1 in self.list_of_dicts[0].keys(): #key for dict in dict1
											for item in self.list_of_dicts[0][key1]:
												if row[key] == str(num) and row[key1].upper() == item.upper() if not item.isdigit() else item:
													for cats in self.print_cat_dict['category']:
														
														data.append(f'for match: {num}; {cats} match is {row[cats]}')
	#												data.append((key,num,key1,item,))
											
						return data
									
							
						
						
							
			
			
			
			
