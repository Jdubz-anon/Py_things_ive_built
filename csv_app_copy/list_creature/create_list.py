import csv
from collections import ChainMap
import parser.final_parser as fp 
import numpy as arr


ent = 'list category State Data.Rates.Property.All 4000-4100'
ent = 'list State alabama Year 1999-2015 category Data.Population'
ent = 'list category State Data.Rates.Property.All 4000-4500'
class ListCreator(fp.Parser3):
		def __init__(self, entry_var, file, *args):
			super().__init__(entry_var, *args)
			self.entry_var = entry_var.split()
			#master_file
			self.file = file
#			self.csv_file = None
			
			
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
						
						if len(self.list_of_dicts) == 2:
							key_map = list(ChainMap(self.print_cat_dict,self.list_of_dicts[0],self.list_of_dicts[1],
											self.rangedict[0]))
							
							for row in csv_file:
								for num in range(int(self.rangedict[0][key_map[0]][0]),
								int(self.rangedict[0][key_map[0]][1]) + 1):
									for val1 in self.list_of_dicts[0][key_map[2]]:
										for val2 in self.list_of_dicts[1][key_map[1]]:
											if all([ row[key_map[0]] == str(num),
  											(row[key_map[2]].upper()  == val1.upper()) ,
   												(row[key_map[1]].upper()  == val2.upper()) ,
   												]):
   												for cat in self.print_cat_dict[key_map[3]]:
   													data.append(row[cat])						
							return data
						
						elif len(self.list_of_dicts) == 1:
							mapped_keys = list(ChainMap(self.print_cat_dict,self.list_of_dicts[0],self.rangedict[0]))
							for row in csv_file:
								for num in range(int(self.rangedict[0][mapped_keys[0]][0]), 
									int(self.rangedict[0][mapped_keys[0]][1])+1):
									for val in self.list_of_dicts[0][mapped_keys[1]]:
										if all([row[mapped_keys[0]]==str(num),
												row[mapped_keys[1]].upper() == val.upper()]):	
											for cat in self.print_cat_dict[mapped_keys[2]]:
												data.append(row[cat])
							return data
						
						elif not self.list_of_dicts:
							key_map = list(ChainMap(self.print_cat_dict,self.rangedict[0]))
							for row in csv_file:
								array = arr.arange(int(self.rangedict[0][key_map[0]][0]),
													int(self.rangedict[0][key_map[0]][1]), 0.1)
								converted_array = array.astype('f')
#								for num in range(int(self.rangedict[0][key_map[0]][0]),
#								int(self.rangedict[0][key_map[0]][1])+1):
								if float(row[key_map[0]]) in converted_array:
									for cat in self.print_cat_dict[key_map[1]]:
										data.append((row[cat], row[key_map[0]]))
#								data.append(row[key_map[0]])
								
								
							return data
							
							
#					else:
#						if len(self.list_of_dicts) == 3:
#							key_map = list(ChainMap(self.list_of_dicts[0],self.list_of_dicts[1],self.list_of_dicts[2],
#							self.print_cat_dict))
							
							
													


#####do not erase under this line!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!########

##				if len(self.entry_var) >= 3:
##					self.parse()
##					data = list()
##					if self.rangedict:
##						for row in csv_file:
##							for dicts in self.rangedict:
##								for key in dicts.keys(): #key for dict in rangedict
##									for num in range(int(dicts[key][0]), int(dicts[key][1]) + 1):							
##										for key1 in self.list_of_dicts[0].keys(): #key for dict in dict1
##											for item in self.list_of_dicts[0][key1]:
##												if row[key] == str(num) and row[key1].upper() == item.upper() if not item.isdigit() else item:
##													for cats in self.print_cat_dict['category']:
##														
##														data.append(f'for match: {num}; {cats} match is {row[cats]}')
##	#												data.append((key,num,key1,item,))
##											
##						return data
									
							
						
						
#lc = ListCreator(entry_var=ent, file='/media/jdubzanon/SmallStorage/csv_files/state_crime.csv')
#lc.creatin_da_list()							
			
			
			
			
