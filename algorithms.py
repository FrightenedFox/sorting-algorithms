from math import floor 		# Importing function floor() from the math module

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
	for i in range(start, stop - 1, step):
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

		The sort in-place (i.e. the list itself is modified) and not stable (i.e. the order of two equal 
		elements is not maintained).

		The reverse flag can be set to sort in descending order.'''
	
	length = len(mylist)

	# Creating a heap from the list
	for ind in range(length-2, -1, -1):
		Heapify(mylist, length, ind)

	for i in range(len(mylist)):
	
		# Replacing the first element with the last one 
		if length>1:
			mylist[0], mylist[length-1] = mylist[length-1], mylist[0]

		# Shrink the length of the list
		length -= 1

		# Restoring the rule of the heap
		Heapify(mylist,length)

	# Reversing the list if an appropriate flag is set
	if reverse:
		for index in range(floor(len(mylist)/2)):
			mylist[index], mylist[-index-1] = mylist[-index-1], mylist[index]

	return mylist



def Heapify(mylist, length, j=0):
	''' Restore the rule of the Heap from the perspective of the given index.
	(i.e. checks if children of the index are in the right order) '''

	# Looking through the heap
	while j*2+1<length:
		
		# Indexes of the children
		ch1, ch2 = j*2+1, j*2+2

		# Finding the biggest child of the current parent
		if ch2<length and mylist[ch1] < mylist[ch2]:
			greater_child_ind = ch2
		else:
			greater_child_ind = ch1

		# Repairing the heap if the greatest child is greater than it's parent
		if mylist[j]<mylist[greater_child_ind]:
			mylist[j], mylist[greater_child_ind] = mylist[greater_child_ind], mylist[j]
			j = greater_child_ind
		else:
			break

	return mylist