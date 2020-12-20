def SelectionSort(mylist, reverse = False):
	''' Sort the list in ascending order and return it.

		The sort is in-place (i.e. the list itself is modified) and not stable (i.e. the order of two equal 
		elements is not maintained).

		The reverse flag can be set to sort in descending order.'''

	length = len(mylist)

	# Defining the direction of the sorting
	if reverse:
		start, stop, step = length-1, -1, -1
	else:
		start, stop, step = 0, length, 1

	# Sorting the list from the smallest value to the biggest one 
	for i in range(start, stop, step):
		min_prey, p_index= mylist[i], i 		# min_prey - first value of the unsorted part of the list
												# p_index - index of the min_prey value in the list

		# Looking for smaller elements then min_prey in the unsorted part of the list
		for j in range(i+step, stop, step):	
			if min_prey > mylist[j]:
				min_prey, p_index = mylist[j], j
		# Swapping the first element of the unsorted part of the list with the smallest element in the same part
		mylist[i], mylist[p_index] = mylist[p_index], mylist[i]
	return mylist



def BinaryHeapSort(mylist, reverse = False):
	''' Sort the list in ascending order and return it.

		The sort is not in-place (i.e. the copy of the input list is created) 
		and not stable (i.e. the order of two equal elements is not maintained).

		The reverse flag can be set to sort in descending order.'''

	# Creating a heap from the list
	MakeHeap(mylist)
	
	sort_list = []			# variable for the sorted list
	length = len(mylist)

	for i in range(length):

		# Adding the first (the greatest) element of the heap to the beginning or end of the output list
		if reverse:
			sort_list.append(mylist[0])
		else:
			sort_list.insert(0, mylist[0])

		# Replacing the first element with the last one and deleting the last element 
		if len(mylist)>1:
			mylist[0]=mylist.pop()

		# Looking through the heap
		j = 0
		while j*2+1<len(mylist):
			
			# Finding the biggest child of the current parent
			if j*2+2<len(mylist) and mylist[j*2+1] < mylist[j*2+2]:
				greater_child_ind = j*2+2
			else:
				greater_child_ind = j*2+1

			# Repairing the heap if bigger child is bigger than parent
			if mylist[j]<mylist[greater_child_ind]:
				mylist[j], mylist[greater_child_ind] = mylist[greater_child_ind], mylist[j]
				j = greater_child_ind
			else:
				break
	# Deleting the input list
	del mylist
	return sort_list



def MakeHeap(mylist):
	''' Create the binary heap from the given list and return it.'''

	from math import floor 		# Importing function floor() from the math module

	# Going through the list, starting from the second element
	for el_index in range(1,len(mylist)):
		i = el_index	# el_index - the copy of the "i" variable, not to overwrite it in the following manipulations

		while i>0:
			new_i = floor((i-1)/2)		# Index of the parent of the element with the index "i"

			# If the parent of the current element with the index "i" is smaller than that element, than swap them 
			if mylist[i]>mylist[new_i]:
				mylist[i], mylist[new_i] = mylist[new_i], mylist[i]
				i = new_i
			else:
				break 	# If parent is greater then child then the heap is created
	return mylist
	
"""
a = [3,4, 13, 23, 12, 35,43,2,5,432,6,32,323,7, -14, -23]
#print(MakeHeap(a))
print(SelectionSort(a.copy()))
print(BinaryHeapSort(a.copy()))
"""

def ReadInputFile(path, separator = None):
	''' Return the list of the sequences of the integers from the file in the given path and number of misunderstood 
		words. All float numbers are floored (i.e. rounded to the closest smaller integer).
		
		Return -1 and number of misunderstood words if the file was empty or there was not a single number in the file.
		Return -2 if file was not found.
		Return -3 if any other error appeared.

		The separator can be changed, if numbers in the input file are separated with a special symbol
		(for ex. separator = ","; default: separator = " ").'''

	try:
		lists, err_count = [], 0		# Defining the output list and the variable to count misunderstood numbers
		with open(path,'r') as file:	# Opens the input file and reads it line by line
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
"""
print(ReadInputFile(".\\tests\\initial_test.txt"))

for i in ReadInputFile(".\\tests\\initial_test.txt")[0]:
	print(SelectionSort(i))
"""