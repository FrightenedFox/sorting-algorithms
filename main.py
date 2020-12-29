import test, algorithms as alg, file_handling as f_handl, console_handling as cl_handl
from time import time
import matplotlib.pyplot as plt, numpy as np

def Sort(path_in, path_out, algorithm = 's', 
	captions = True, clear_out_f = True, print_info = True, progress_bar = True):
	''' Sort all sequences in the file with path "path_in" and writes it to the file
	 with the path "path_out". 

	 The sorting algorithm can be specified by the "algorithm" parameter:
	 	's', 'S' - selection sort
	 	'h', 'H' - binary heap sort 

	 If captions flag is set then the output sequences will be labeled.

	 "clear_out_f" flag can be turned off not to clear an output file before 
	 writing down the results.

	 If print_info flag is set then some info about the task will be printed
	 to the console.
	'''

	sequences = f_handl.ReadInputFile(path_in)[0]	# Reading an input file
	counter = 1
	times = []
	if clear_out_f:
		f_handl.PrepareFile(path_out)	# Clearing the output file

	cl_handl.draw_separator(path_in)

	counter = 0
	for sequence in sequences:
		start_time = time()

		if algorithm.lower() == 's':
			array = alg.SelectionSort(sequence)
		elif algorithm.lower() == 'h':
			array = alg.BinaryHeapSort(sequence)

		end_time = time()
		times += [round(end_time-start_time, 4)]

		if captions:
			f_handl.AppendFile(path=path_out, out_list=array, label=counter)
		else:
			f_handl.AppendFile(path=path_out, out_list=array, end='\n')

		counter += 1
		if progress_bar:
			cl_handl.update_progress(counter/len(sequences), path_in)

	if print_info:
		print('')
		cl_handl.task_info(len(sequences), times, path_in, path_out, algorithm.lower())

	return times



def main():
	''' Implementation of all functions and showing the graph of the results. In other words - examples.'''
	# path=".\\tests\\test.txt"

	# Initial test
	Sort('.\\tests\\initial_test.txt', '.\\tests\\initial_result.txt', algorithm = 'S', 
		captions = True, progress_bar = False)

	# Creating an input file for the test
	test.CreateInput(path=".\\tests\\main_test.txt", Nmin = 0, Nmax = 1000, sequences = 100, len_start = 10,
		len_incr = 10, len_mult = 1, complexity = 0)

	# Creating an numpy array of the times of algorithm working time
	sel_times = np.array(Sort('.\\tests\\main_test.txt', '.\\tests\\sel_result.txt', algorithm = 'S', captions = False))
	heap_times = np.array(Sort('.\\tests\\main_test.txt','.\\tests\\heap_result.txt',algorithm = 'H', captions = False))

	# Values for x axes in numpy array format. Similar to np.array(range(100))
	x = np.linspace(0, 100, 100)

	plt.figure('Algorithms comparison')
	plt.scatter(x, sel_times, s=10, c = 'red',  label = 'Selection Sort')
	plt.scatter(x, heap_times, s=10, c = 'green', label = 'Binary Heap Sort')
	plt.xlabel('Number of test')
	plt.ylabel('Time, seconds')
	plt.title('Binary Heap Sort and Selection Sort algorithms comparison')
	plt.legend(loc=2)
	plt.show()
	plt.close()

	print('\nCreating a new set of data...', flush = True)

	test.CreateInput(path=".\\tests\\a_ascending_test.txt", Nmin = 0, Nmax = 50000, sequences = 100, 
		len_start = 10000, len_incr = 0, len_mult = 1, complexity = -1, distrib = 10, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path=".\\tests\\f_random_test.txt", 	Nmin = 0, Nmax = 50000, sequences = 100, 
		len_start = 10000, len_incr = 0, len_mult = 1, complexity =  0, distrib = 10, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path=".\\tests\\a_descending_test.txt",Nmin = 0, Nmax = 50000, sequences = 100, 
		len_start = 10000, len_incr = 0, len_mult = 1, complexity =  1, distrib = 10, dist_incr = 0, dist_mult = 1)

	heap_times_m1 = np.array(Sort('.\\tests\\a_ascending_test.txt','.\\tests\\a_ascending_result.txt',
		algorithm = 'H', captions = False))
	heap_times_0 = np.array(Sort('.\\tests\\f_random_test.txt','.\\tests\\f_random_result.txt',
		algorithm = 'H', captions = False))
	heap_times_1 = np.array(Sort('.\\tests\\a_descending_test.txt','.\\tests\\a_descending_result.txt',
		algorithm = 'H', captions = False))

	plt.figure('Inputs comparison')
	plt.scatter(x, heap_times_m1, s=10, c = 'red',  label = 'almost ascending')
	plt.scatter(x, heap_times_0, s=10, c = 'green', label = 'fully random')
	plt.scatter(x, heap_times_1, s=10, c = 'blue', label = 'almost descending')
	plt.xlabel('Number of test')
	plt.ylabel('Time, seconds')
	plt.title('Inputs comparison for Binary Heap sorting algorithm')
	plt.legend(loc=2)
	plt.show()



if __name__ == "__main__":
    main()