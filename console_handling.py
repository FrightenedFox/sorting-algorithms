import sys
# The next function is not written by Vitalii Morskyi (just modified)
# Source: https://stackoverflow.com/questions/3160699/python-progress-bar
def update_progress(progress, path_in):
	''' Displays or updates a console progress bar. WORKS ONLY WITH CONSOLE
	Accepts a float between 0 and 1. Any int will be converted to a float.
	A value under 0 represents a 'halt'.
	A value at 1 or bigger represents 100%.'''

	barLength = 10 # Modify this to change the length of the progress bar
	status = ""
	if isinstance(progress, int):
		progress = float(progress)
	if not isinstance(progress, float):
		progress = 0
		status = "error: progress var must be float\r\n"
	if progress < 0:
		progress = 0
		status = "Halt...\r\n"
	if progress >= 1:
		progress = 1
		status = "Gotowy...\r\n"
	block = int(round(barLength*progress))
	text = "\rPrzetwarzanie pliku \"{3}\" : [{0}] {1}% {2}".format( "#"*block + 
		"-"*(barLength-block), round(progress*100,1), status, path_in)
	sys.stdout.write(text)
	sys.stdout.flush()



def draw_separator(path):
	''' This function draws a "pretty" separator between tasks'''
	heading = " Nowe zadanie z pliku: \"{}\" ".format(path)
	separator = '-'*5 + heading + '-'*(115 - len(heading))
	print('\n\n\n\n' + separator + '\n')


def task_info(number_of_sequences, time_results, path_in, path_out, algotithm_type):
	''' Print some useful info about current task to the console '''

	if str(number_of_sequences)[-2:] in ['11', '12', '13', '14']:		# excluding -teen numbers
		teened = True
	else:
		teened = False
	last_digit=str(number_of_sequences)[-1]

	if last_digit=='1' and not teened:
		insert_text = 'wejsciowy ciag'
	elif last_digit in ['2', '3', '4'] and not teened:
		insert_text = 'wejsciowy ciagi'
	else:
		insert_text = 'wejsciowych ciagow'

	algotithm = ''
	if algotithm_type == 's':
		algotithm = 'sortowanie przez wybieranie'
	elif algotithm_type == 'h':
		algotithm = 'sortowanie kopcowe'

	time_used = round(sum(time_results),3)
	avarage_time_used = round(time_used/number_of_sequences, 5)
	print("Rozpoznano {0} {1} w pliku \"{2}\". ".format(number_of_sequences, insert_text, path_in)+
		"\nWszystkie odpowiedzi zostaly zapisane w pliku \"{}\". ".format(path_out) +
		"\nWykonano {}.".format(algotithm)+
		"\nCzas roboty algorytmu wynosi {} s.".format(time_used) + 
		"\nSredni czas przetwarzania jednego ciagu wynosi {} s.\n".format(avarage_time_used), flush = True)