from collections import ChainMap




#ent = 'list category State Data.Rates.Property.All 1000-2000 Year 1990-2000 Data.Rates.Property.Burglary 300-400'
#ent = "list category Data.Rates.Property.All State new-york Year 2000-2010 Data.Rates.Property.Burglary 355-400"
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
	
	
	def parse(self):
		for i in range(len(self.split_input)):
			if i % 2 != 0 and self.split_input[i] == 'category':
				self.print_cat_dict[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]
			
			elif i % 2 != 0 and self.split_input[i] != 'category':
				
				if not self.dict1.keys():
					self.dict1[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]	
				
				elif self.dict1.keys and not self.dict2.keys():
					self.dict2[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')] 
				
				else:
					self.dict3[self.split_input[i]] = [value.replace('-',' ') for value in self.split_input[i + 1].split('&')]

			


		key_map = list(ChainMap(self.dict3,self.dict2,self.dict1))
		
		if self.dict1.keys():
			
			if self.dict1[key_map[0]][0][0].isdigit():
				for item in self.dict1[key_map[0]]:
					self.dict1[key_map[0]] = item.split()
					if len(self.dict1[key_map[0]]) > 1:
						self.rangedict.append(self.dict1)
					else:
						self.list_of_dicts.append(self.dict1)
			else:
				if not self.dict1 in self.list_of_dicts:
					self.list_of_dicts.append(self.dict1)
			
		if self.dict2.keys():
			
			if self.dict2[key_map[1]][0][0].isdigit():
				for item in self.dict2[key_map[1]]:
					self.dict2[key_map[1]] = item.split()
					if len(self.dict2[key_map[1]]) > 1:
						self.rangedict.append(self.dict2)
					else:
						if all([self.dict2 not in self.list_of_dicts, self.dict2 not in self.rangedict]):
							self.list_of_dicts.append(self.dict2)
			else:
				if all([self.dict2 not in self.rangedict, self.dict2 not in self.list_of_dicts]):
					self.list_of_dicts.append(self.dict2)
		
		
		
		if self.dict3.keys():
			
			if self.dict3[key_map[2]][0][0].isdigit():
				for item in self.dict3[key_map[2]]:
					self.dict3[key_map[2]] = item.split()
					if len(self.dict3[key_map[2]]) > 1:
						self.rangedict.append(self.dict3)
					else:
						self.list_of_dicts.append(self.dict3)
			else: 
				if all([self.dict3 not in self.list_of_dicts, self.dict3 not in self.rangedict]):
					self.list_of_dicts.append(self.dict3)

				
#		print("dict1 : " ,self.dict1)
#		print('dict2 : ' , self.dict2)
#		print('dict3 : ', self.dict3)
##		print(key_map)
#		print(self.rangedict)
#		print(self.list_of_dicts)






#p = Parser3(ent)
#p.parse()





	

