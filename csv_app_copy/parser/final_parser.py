fields = ['state','category','date', 'deathrate']

ent = 'list category Date.Total.Violent.Robbery State alabama Year 1995-2005'

#pass shell ent_var and csv_reader
class Parser3:
	def __init__(self, inputs): 

		self.print_cat_dict = dict()
		self.dict1 = dict()
		self.dict2 = dict()
		self.dict3 = dict()
		self.rangedict = list()
		self.list_of_dicts = list()
		self.split_input = inputs.split()
		self.func_dict = {
			'list': None,
			'connect': None,
			'peek': None,
			'graph': None
		}
#		self.func_list = list(filter(lambda func : func in self.func_dict, self.split_input))	
				
	
	
	def parse(self):
		for i in range(len(self.split_input)):
			if i % 2 != 0 and self.split_input[i] == 'category':
#				loc = self.split_input.index(item)
				self.print_cat_dict[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]
#				print(self.print_cat_dict)
			elif i % 2 != 0 and self.split_input[i] != 'category':
				if not self.dict1.keys():
#					loc = self.split_input.index(item)
					self.dict1[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]	
				elif self.dict1.keys and not self.dict2.keys():
#					loc = self.split_input.index(item)
					self.dict2[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')] 
				else:
#					loc = self.split_input.index(item)
					self.dict3[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]


		# checking for date range in dictionary/	organizing arguements	
		if self.dict1.keys():
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
		if self.dict2.keys():
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
		if self.dict3.keys():
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




	

