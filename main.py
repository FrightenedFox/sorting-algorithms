import algorithms as alg, file_handling as f_handl

def Search(path_in, path_out, algorithm = 's', captions = True, clear_out_f = True):
	sequences = f_handl.ReadInputFile(path_in)[0]
	counter = 1
	if clear_out_f:
		f_handl.PrepareFile(path_out)
	for sequence in sequences:
		if algorithm.lower() == 's':
			array = alg.SelectionSort(sequence)
		elif algorithm.lower() == 'h':
			array = alg.BinaryHeapSort(sequence)			
		print(array)
		if captions:
			f_handl.AppendFile(path=path_out, out_list=array, label=counter)
		else:
			f_handl.AppendFile(path=path_out, out_list=array, end='\n')
		counter += 1

Search('.\\tests\\initial_test.txt', '.\\tests\\initial_result.txt', algorithm = 'H', captions = True)