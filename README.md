# **Heapsort vs Selection sort**  
*By Vitalii Morskyi*  

***

This project is a part of the curriculum in "Algorytmy i Struktury danych"
of the Polytechnic University of Rzeszów, Poland.  
  
## The main goal of the project  
  
To implement and analyze the selection sort and binary heap sort algorithms, compare their complexities and plot the
results of the tests.  

## Navigation through files and folders  
  
A detailed explanation of my work can be found in the file `"Sprawozdanie.pdf"` or `"report.docx"`.  

The main file of the program is named `"main.py"`. There you can find some demonstrative tests and comparisons.  
In the file `"algorithms.py"` you can find both sorting algorithms.  

There is also a couple of other files, which helps to get everything together:    
 * `"console_handling.py"` - functions to show some useful info in the console;
 * `"file_handling.py"` - reading sequences from & writing them to the file;
 * `"test.py"` - contains everything needed to create a testing sample of input sequences.
  
In the file `"block-diagram.drawio"` you can find the block diagrams of the following functions:
 * `SelectionSort()`
 * `Heapify()`
 * `BinaryHeapSort()`
  
The folder `tests` is used to keep input and output files.  
In the folder `Images` all pictures used in the project are saved.  
  
## Recommendations regarding file executing  

1. If the progress bar in your environment looks like this:  
	`Przetwarzanie pliku ".\tests\input_worst_scenario.txt" : [----------] 0.0%  
	Przetwarzanie pliku ".\tests\input_worst_scenario.txt" : [----------] 5.0%  
	Przetwarzanie pliku ".\tests\input_worst_scenario.txt" : [#---------] 10.0%  
	Przetwarzanie pliku ".\tests\input_worst_scenario.txt" : [##--------] 15.0% `  
	(repeats instead of changing in one line),  
	than probably you would like to turn off the progress bar at all. 
	To do so, please set the flag `progress_bar` in the function `Sort()` (file `"main.py"`) to `false`. 
2. If you don't have modules `numpy` and `matplotlib` then, in order to see the plots of the comparisons, you have
	to install them.  
	[An official guide of installing `matplotlib`](https://matplotlib.org/3.1.1/users/installing.html)  
	[An official guide of installing `numpy`](https://numpy.org/install/)  
  
## Conclusions  
  
In this project, I analyzed two algorithms for sorting numeric sequences with complexities `𝜃(𝑛^2)` and `𝜃(𝑛log𝑛)`,
namely selection sort and Binary Heap sort.  
The result of the processed work is a program that can:  
 - load input data from various text files and `csv` files;  
 - create random input strings or strings with different levels of worst-case/best-case performance;  
 - write out sorted strings to files;  
 - demonstrate the complexity of sorting algorithms;  
 - demonstrate the dependence of the sort time on the structure of the input data.  
  
Flowcharts, pseudocodes and detailed diagrams of the operation of both algorithms, graphs for comparing the time complexity of the algorithms and the dependence of the sort time on the input file were also created.  
  
***
  
![Project logo](/Images/logo.jpg)