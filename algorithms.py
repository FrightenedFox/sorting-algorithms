def SelectionSort(array, increasing = True):
	length = len(array)
	if increasing:
		start, stop, step = 0, length, 1
	else:
		start, stop, step = length-1, -1, -1
	for i in range(start, stop, step):
		prey, p_index= array[i], i
		for j in range(i+step, stop, step):
			if prey > array[j]:
				prey, p_index = array[j], j
		array[i], array[p_index] = array[p_index], array[i]
	return array

print(SelectionSort([3,4, 12, 23, 12, 32,43,2,3,432,4,32,323,4], False))