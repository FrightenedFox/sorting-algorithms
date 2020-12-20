def ReadInputFile(path, separator = None):
	''' Return the list of the sequences of the integers from the file in the given path and number of misunderstood 
		words. All float numbers are floored (i.e. rounded to the closest smaller integer).
		
		Return -1 and number of misunderstood words if the file was empty or there was not a single number in the file.
		Return -2 if file was not found.
		Return -3 if any other error appeared.

		The separator can be changed, if numbers in the input file are separated with a special symbol
		(for ex. separator = ","; default: separator = " ").'''	
	#".\\tests\\initial_test.txt"
	try:
		lists, err_count = [], 0		# Defining the output list and the variable to count misunderstood numbers
		with open(path,mode='r') as file:	# Opens the input file and reads it line by line
			for line in file:
				this_sequence = []
				for word in line.strip().split(separator):	# Cutting the sequence with the respect to the separator
					try:
						this_sequence.append(int(word))
					except ValueError:
						err_count += 1
				if this_sequence != []:
					lists.append(this_sequence)
		if lists != []:
			return lists, err_count
		else:
			return -1, err_count 	# File is empty, number of missed numbers/words
	except FileNotFoundError:
		return -2					# File is not found
	except:
		return -3					# Something else went wrong



def PrepareOutputFile(path):
	''' Cleaning (or creating) the file in the given path '''

	with open(path,mode='w', encoding='utf-8') as file:		
		pass



def AppendOutputFile(path, out_list, label=None):
	''' Adds the list out_list to the end of the file in the given path. 

		If label is given then the output will be labeled.'''

	with open(path,mode='a', encoding='utf-8') as file:
		if label:
			if type(label)==int:
				file.write('Sequence #'+str(label)+':\n')
			else:
				file.write('Sequence \''+str(label)+'\':\n')
		file.write(str(out_list)[1:-1]+'\n\n')