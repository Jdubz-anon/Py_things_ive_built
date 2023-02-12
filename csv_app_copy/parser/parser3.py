fields = ['state','category','date', 'deathrate']

ent = 'state new-york&new-jersey date 1999-2020 category murder deathrate 1998'

#pass shell ent_var and csv_reader
class Parser3:
	def __init__(self, inputs, csv_reader): 

		self.print_cat_dict = dict()
		self.dict1 = dict()
		self.dict2 = dict()
		self.dict3 = dict()
		self.rangedict = list()
		self.list_of_dicts = list()
		self.split_input = inputs.split()
		self.csv_reader = csv_reader
		self.func_dict = {
			'list': None,
			'connect': None,
			'peek': None,
			'graph': None
		}
		self.func_list = list(filter(lambda func : func in self.func_dict, self.split_input))	
		
	
	
	def parse(self):
		for item in self.split_input:
			if item == 'category':
				loc = self.split_input.index(item)
				self.print_cat_dict[item] = [value.replace('-',' ') for value in self.split_input[loc+1].split('&')]
		#		print(print_cat_dict)
				#need to add .filednames to csv_reader
			elif item in self.csv_reader and item != 'category':
				if not self.dict1.keys():
					loc = self.split_input.index(item)
					self.dict1[item] = [value.replace('-',' ') for value in self.split_input[loc+1].split('&')]	
		#			print(dict1)
				elif self.dict1.keys and not self.dict2.keys():
					loc = self.split_input.index(item)
					self.dict2[item] = [value.replace('-',' ') for value in self.split_input[loc+1].split('&')] 
		#			print(dict2)
				else:
					loc = self.split_input.index(item)
					self.dict3[item] = [value.replace('-',' ') for value in self.split_input[loc+1].split('&')]
		#			print(dict3)
									
		# checking for date range in dictionary/	organizing arguements	
		for items in self.dict1.values():
			for item in items:
				if item[0].isdigit():
					#this said dict2.keys() i changed to dict1.keys()
					for key in self.dict1.keys():
						self.dict1[key] = item.split(' ')
						if len(self.dict1[key]) > 1:
							self.rangedict.clear()
							self.rangedict.append(self.dict1)
						else:
							self.list_of_dicts.append(self.dict1)
				else:
					 if self.dict1 not in self.list_of_dicts:
					 	self.list_of_dicts.append(self.dict1)

		# checking for date range in dictionary/ organizing arguements
		for items in self.dict2.values():
			for item in items:
				if item[0].isdigit():
					for key in self.dict2.keys():
						self.dict2[key] = item.split(' ')
						if len(self.dict2[key]) > 1:
							self.rangedict.clear()
							self.rangedict.append(self.dict2)
						else:
							self.list_of_dicts.append(self.dict2)
				else:
					 if self.dict2 not in self.list_of_dicts:
					 	self.list_of_dicts.append(self.dict2)
					 	


		## checking for date range in dictionary/ orgainizing arguements
		for items in self.dict3.values():
			for item in items:
				if item[0].isdigit():
					for key in self.dict3.keys():
						self.dict3[key] = item.split(' ')
						if len(self.dict3[key]) > 1:
							self.rangedict.clear()
							self.rangedict.append(self.dict3)
						else:
							self.list_of_dicts.append(self.dict3)
				else:
					 if self.dict3 not in self.list_of_dicts:
					 	self.list_of_dicts.append(self.dict3)

# ent is shell.entry_var.get()
# fields is list_creator.csv_reader
parser = Parser3(ent,fields)
parser.parse()
print(parser.list_of_dicts)
print(parser.rangedict)




	

