from file_handling import *
import random, algorithms

def CreateInput(path=".\\tests\\test.txt", complexity = 0, Nmin = 0, Nmax = 1000, repeats = 10,
	len_start = 10, len_incr = 1, len_mult = 1):
	PrepareFile(path)
	for i in range(repeats):
		if complexity == 0:
			AppendFile(path = path, out_list = random.choices(range(Nmin, Nmax), k=len_start), end='\n')
		len_start += len_incr
		len_start *= len_mult

path=".\\tests\\test.txt"
CreateInput(path)

sequences = ReadInputFile(path)[0]

for sequence in sequences:
	array = algorithms.SelectionSort(sequence)
	print(array)
	AppendFile(path=path, out_list=array)