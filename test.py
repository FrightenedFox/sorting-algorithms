import random, file_handling as f_handl


def CreateInput(path=".\\tests\\test.txt", complexity = 0, Nmin = 0, Nmax = 1000, sequences = 10,
	len_start = 10, len_incr = 1, len_mult = 1, distrib = 0, dist_incr = 0, dist_mult = 1):
	''' Create a file with some input sequences depending on given parameters.
	
	path 		- path of the output file;
	complexity 	- the type of input data:
		0  - random sequence of values (default)
		-1 - almost ascending sequence of values, but some elements may not be on their positions
		1  - almost descending sequence of values, but some elements may not be on their positions
	Nmin 		- minimal possible value
	Nmax + 1	- maximum possible value 
	sequences	- number of sequences in the resulting file
	len_start 	- starting length of the line
	len_incr	- line length increment after each line
	len_mult	- line length multiplication after each line

	distrib 	- (only for complexity values -1 or 1)determines the degree of the entropy of the 
		sequence (the higher - the more random)
	dist_incr	- distribution (distrib) value increment after each line
	dist_mult	- distribution (distrib) value multiplication after each line
	'''

	f_handl.PrepareFile(path)
	for i in range(sequences):
		if complexity == 0:
			f_handl.AppendFile(path = path, out_list = random.choices(range(Nmin, Nmax), k=len_start), end='\n')

		elif complexity == -1:

			sequence = CreateSpecialSequence(start=Nmin, stop=Nmax, length=len_start, distrib=distrib)
			f_handl.AppendFile(path = path, out_list = sequence, end='\n')

		elif complexity == 1:
			sequence = CreateSpecialSequence(start=Nmax, stop=Nmin, length=len_start, distrib=distrib)
			f_handl.AppendFile(path = path, out_list = sequence, end='\n')

		len_start += len_incr
		len_start *= len_mult
		distrib += dist_incr
		distrib *= dist_mult



def CreateSpecialSequence(start=0, stop=None, length=None, distrib=None):
	''' Return sequence of almost descending or ascending (depending on the start and stop parameters) elements 
	(i.e. the sequence is not sorted perfectly, most of the elements are sorted). 
	
	The distribution parameter determine the degree of the entropy of the sequence (the higher - the more random).'''

	sequence = []
	min_point = min(start, stop)
	if distrib == None:
		distrib = 0
	# represents correlation between the length of the line and the distance from start to stop point
	coef = (abs(stop-start)-distrib)/length 	

	# determining if we are moving forward or backward
	direction = int(abs(stop-start)/(stop-start))
	if direction==1:
		begin, end = 0, length
	else:
		begin, end = length, 0

	# adding a random element from the range 'distribution'
	for i in range(begin, end, direction):
		sequence.append(random.randint(min_point+int(i*coef), min_point+int(i*coef)+distrib))
	return sequence