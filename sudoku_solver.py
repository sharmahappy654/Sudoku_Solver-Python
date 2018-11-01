import sys
from helper import *
ip_file = sys.argv[1]  ## storing filename given from command line
ip_matrix = []


with open(ip_file, 'r') as file:         ## opening file in read mode
	for line in file:                     ## taking line input from file
		ip_matrix.append(custom_split(line))    ## splitting line and storing as list

matrix  = [[i for i in range(0,9)] for i in range(0,9)] ## creating 2D list using list comprehension
matrix[1][1] = -1

for i in range(0,9):
	for j in range(0,9):
		if ip_matrix[i][j] == '0' or ip_matrix[i][j] == 0:
			matrix[i][j] = ' '	
		else:
			matrix[i][j] = int(ip_matrix[i][j])

# print("you entered ",ip)

print_sudoku(matrix)
print("*****************************************")
print_sudoku(solve(matrix))


	