import csv
from collections import ChainMap
import parser.final_parser as fp 
import numpy as arr
import pathlib

#ent = 'list category State Year <1961'
#ent = 'list category State Year 1960-1975 Data.Rates.Property.Burglary >2500'

class ListCreator(fp.Parser3):
		def __init__(self, entry_var, file_path, *args):
			super().__init__(entry_var, *args)
			#master_file
			self.file_path = file_path
			self.range1 = None
			self.range2 = None
			self.range3 = None			
		
		
		def creatin_da_list(self):
			with self.file_path.open() as fi:
				csv_file = csv.DictReader(fi)
				if len(self.split_input) == 2:
					data = list()
					if self.split_input[-1] == 'cats':
						for names in csv_file.fieldnames:
							data.append(names)
						return data
					
					elif self.split_input[-1] == 'catx':
						count = 0
						data = list()
						for row in csv_file:
							count += 1
							if count == 2:
								for values in csv_file.fieldnames:
									data.append(f"{values} :  {row[values]}")			
						return data
				
				
				if len(self.split_input) > 2:		
					self.parse()
					if len(self.rangedict) + len(self.list_of_dicts) == 3:
						if len(self.rangedict) == 3:
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict,self.rangedict[2], self.rangedict[1], self.rangedict[0]))
							
							self.range1 = arr.arange(float(self.rangedict[0][key_map[0]][0]) ,
							float(self.rangedict[0][key_map[0]][1]) + 1,0.1).astype('f')
							
							self.range2 = arr.arange(float(self.rangedict[1][key_map[1]][0]), 
							float(self.rangedict[1][key_map[1]][1]) + 1, 0.1).astype('f')
							
							self.range3 = arr.arange(float(self.rangedict[2][key_map[2]][0]), 
							float(self.rangedict[2][key_map[2]][1]) + 1, 0.1).astype('f')

							filter1 = filter(lambda row : float(row[key_map[0]]) in self.range1, csv_file )

							filter2 = filter(lambda row: float(row[key_map[1]]) in self.range2, filter1)

							filter3 = filter(lambda row: float(row[key_map[2]]) in self.range3, filter2)

							for cats in self.print_cat_dict[key_map[3]]:
								for rows in filter3:
									data.append(rows[cats])
							
							return data
						
						elif all([   (len(self.rangedict) == 2),
									(len(self.list_of_dicts) == 1)    ]):
							
							data = list()
								
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[0], self.rangedict[1], self.rangedict[0]))

							self.range1 = arr.arange(float(self.rangedict[0][key_map[0]][0]), 
							float(self.rangedict[0][key_map[0]][1]) + 1, 0.1).astype('f')
							
							self.range2 = arr.arange(float(self.rangedict[1][key_map[1]][0]), 
							float(self.rangedict[1][key_map[1]][1]) + 1, 0.1).astype('f')
						    
							filter1 = filter(lambda row: float(row[key_map[0]]) in self.range1, csv_file)

							filter2 = filter(lambda row: float(row[key_map[1]]) in self.range2, filter1)
						    
							for val in self.list_of_dicts[0][key_map[2]]:
								filter3 = filter(lambda row: 

								any([row[key_map[2]].upper() == val.upper(),
								float(row[key_map[2]]) > float(val[1:]) if '>' in val else None,
								float(row[key_map[2]]) < float(val[1:]) if '<' in val else None
								
								]), filter2)

							for cats in self.print_cat_dict[key_map[3]]:
								for rows in filter3:
									data.append(rows[cats])

							return data
							    

						elif all([len(self.rangedict) == 1,
								len(self.list_of_dicts) == 2]):
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[1], self.list_of_dicts[0], self.rangedict[0]))
							
							self.range1 = arr.arange(   float(self.rangedict[0][key_map[0]][0]),
														float(self.rangedict[0][key_map[0]][1]) + 1, 0.1     ).astype('f')
							
							filter1 = filter(lambda row: float(row[key_map[0]]) in self.range1, csv_file)
							
							for first_val in self.list_of_dicts[0][key_map[1]]:
								filter2 = filter(lambda row: 

								any([row[key_map[1]].upper() == first_val.upper(),
								float(row[key_map[1]]) > float(first_val[1:]) if '>' in first_val else None,
								float(row[key_map[1]]) < float(first_val[1:]) if '<' in first_val else None
								
								]), filter1)
									
							for second_val in self.list_of_dicts[1][key_map[2]]:
								filter3 = filter(lambda row: 

								any([row[key_map[2]].upper() == second_val.upper(),
								float(row[key_map[2]]) > float(second_val[1:]) if '>' in second_val else None,
								float(row[key_map[2]]) < float(second_val[1:]) if '<' in second_val else None
								
								]), filter2)
								

							for cats in self.print_cat_dict[key_map[3]]:
								for row in filter3:
									data.append(row[cats])

							return data
							

						elif len(self.list_of_dicts) == 3:
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[2], 
							self.list_of_dicts[1], self.list_of_dicts[0]))
							
							for first_val in self.list_of_dicts[0][key_map[0]]:
								filter1 = filter(lambda row: 

								any([row[key_map[0]].upper() == first_val.upper(),
								float(row[key_map[0]]) > float(first_val[1:]) if '>' in first_val else None,
								float(row[key_map[0]]) < float(first_val[1:]) if '<' in first_val else None
								
								
								]), csv_file)
								
							for second_val in self.list_of_dicts[1][key_map[1]]:
								filter2 = filter(lambda row: 

								any([row[key_map[1]].upper() == second_val.upper(),
								float(row[key_map[1]]) > float(second_val[1:]) if '>' in second_val else None,
								float(row[key_map[1]]) < float(second_val[1:]) if '<' in second_val else None
								
								
								]), filter1)
								 
							for third_val in self.list_of_dicts[2][key_map[2]]:
								filter3 = filter(lambda row: 

								any([row[key_map[2]].upper() == third_val.upper(),
								float(row[key_map[2]]) > float(third_val[1:]) if '>' in third_val else None,
								float(row[key_map[2]]) < float(third_val[1:]) if '<' in third_val else None
								
								
								]), filter2)
								
							for cats in self.print_cat_dict[key_map[3]]:
								for row in filter3:
									data.append(row[cats])

							return data
							
					elif len(self.rangedict) + len(self.list_of_dicts) == 2:
						if len(self.rangedict) == 2:
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.rangedict[1], self.rangedict[0]))	
							
							self.range1 = arr.arange( float(self.rangedict[0][key_map[0]][0]),
							float(self.rangedict[0][key_map[0]][1]) + 1, 0.1 ).astype('f')
							
							self.range2 = arr.arange( float(self.rangedict[1][key_map[1]][0]),
							float(self.rangedict[1][key_map[1]][1]) + 1, 0.1 ).astype('f')
							
							filter1 = filter(lambda row: float(row[key_map[0]]) in self.range1, csv_file)
							
							filter2 = filter(lambda row: float(row[key_map[1]]) in self.range2, filter1)
							
							for cats in self.print_cat_dict[key_map[2]]:
								for row in filter2:
									data.append(row[cats])

							return data
								
						elif all([len(self.rangedict) == 1,
								len(self.list_of_dicts) == 1]):
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[0], self.rangedict[0]))														
							
							self.range1 = arr.arange( float(self.rangedict[0][key_map[0]][0]),
							float(self.rangedict[0][key_map[0]][1]) + 1, 0.1).astype('f')
							
							filter1 = filter(lambda row: float(row[key_map[0]]) in self.range1, csv_file)
							
							for first_val in self.list_of_dicts[0][key_map[1]]:
								filter2 = filter(lambda row: 

								any([row[key_map[1]].upper() == first_val.upper(),
								float(row[key_map[1]]) > float(first_val[1:]) if '>' in first_val else None,
								float(row[key_map[1]]) < float(first_val[1:]) if '<' in first_val else None
								
								
								]), filter1)
								
							for cats in self.print_cat_dict[key_map[2]]:
								for row in filter2:
									data.append(row[cats])
							print(data)
							return data							
														
	#					
						elif len(self.list_of_dicts) == 2:
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[1], self.list_of_dicts[0]))
							
							for first_val in self.list_of_dicts[0][key_map[0]]:
								filter1 = filter(lambda row: 

								any([row[key_map[0]].upper() == first_val.upper(),
								float(row[key_map[0]]) > float(first_val[1:]) if '>' in first_val else None,
								float(row[key_map[0]]) < float(first_val[1:]) if '<' in first_val else None

								
								]), csv_file)
								
							for second_val in self.list_of_dicts[1][key_map[1]]:
								filter2 = filter(lambda row: 

								any([row[key_map[1]].upper() == second_val.upper(),
								float(row[key_map[1]]) > float(second_val[1:]) if '>' in second_val else None,
								float(row[key_map[1]]) < float(second_val[1:]) if '<' in second_val else None
								
								
								]), filter1)
								
							for cats in self.print_cat_dict[key_map[2]]:
								for row in filter2:
									data.append(row[cats])

							return data		
							
							
					elif len(self.rangedict) + len(self.list_of_dicts) == 1:
						if self.rangedict:
							
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.rangedict[0]))														
							
							self.range1 = arr.arange( float(self.rangedict[0][key_map[0]][0]),
							float(self.rangedict[0][key_map[0]][1]) + 1, 0.1 ).astype('f')

							filter1 = filter(lambda row: float(row[key_map[0]]) in self.range1, csv_file)
							
							for cats in self.print_cat_dict[key_map[1]]:
								for row in filter1:
									data.append(row[cats])
							
							return data 
							
						elif self.list_of_dicts:
															
							data = list()
							
							key_map = list(ChainMap(self.print_cat_dict, self.list_of_dicts[0]))
							
							for first_val in self.list_of_dicts[0][key_map[0]]:
								filter1 = filter(lambda row: 
								
								any( [row[key_map[0]].upper() == first_val.upper(),
								float(row[key_map[0]]) > float(first_val[1:]) if '>' in first_val else None,
								float(row[key_map[0]]) < float(first_val[1:]) if '<' in first_val else None 
								                                   
								                                   
								 ]), csv_file)
					
							
							for cats in self.print_cat_dict[key_map[1]]:
								for row in filter1:
									data.append(row[cats])
							
							return data
							
							



#lc = ListCreator(entry_var=ent, file_path=pathlib.Path('/media/jdubzanon/SS/csv_files/state_crime.csv'))
#lc.creatin_da_list()




							
						
						

			
			
			
