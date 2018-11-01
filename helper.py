def custom_split(line):
	tmp_list = []
	space = 0
	for i in line:
		if i == ' ' and space == 0:
			space = 1
			continue
		else:
			tmp_list.append(i)
			space = 0;

	return tmp_list;

def compress_coordinate(matrix):
	count = 0
	count_list = []
	for line in matrix:
		for i in line:
			if i != ' ':
				count+=1
		count_list.append(count)
		count = 0
	
	sorted_list = sorted(count_list, reverse = True)

	it = 0
	ind = 0
	while it < len(sorted_list):
		ind = count_list.index(sorted_list[it])
		sorted_list[it] =  ind
		count_list[ind] = 0
		it+=1

	return sorted_list

def print_sudoku(matrix):
	for i in range(0,9):
		for j in range(0,9):
			print(matrix[i][j],end = ' ')
			if j == 2 or j ==5:
				print("|",end = ' ')
		print()	 
		if i == 2 or i ==5:
			for k in range(0,11):
			 print('-',end = ' ')

			print()

def check_col(num, col, sudoku):
	for i in range(0,9):
		if sudoku[i][col] == num:
				return True
	return False			

def check_row(num, row, sudoku):
	for i in range(0,9):
		if sudoku[row][i] == num:
			return True
	return False		


def solve_mat3X3(row, col, sudoku):
	number_list = [0 for i in range(0,11)]
	number_list[0] = 1
	missing_numbers = []
	for i in range(0,3):
		for j in range(0,3):
			if sudoku[row+i][col+j] != ' ':
				number_list[sudoku[row+i][col+j]] = 1
	for i in range(1,10):
		if number_list[i] == 0:
			missing_numbers.append(i)
	
		for i in range(0,3):
			for j in range(0,3):
				if sudoku[row+i][col+j] == ' ':
					for num in missing_numbers:
						if not check_row(num,row+i, sudoku) and not check_col(num, col+j, sudoku):	
							sudoku[row+i][col+j] = num
							missing_numbers.remove(num)	

## function that solves given sudoku
def solve(sudoku):
	row = 0
	col = 0
	empty_cells = 0;
	remaining_cells = 0;
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j] == ' ':
				empty_cells+=1

	for i in range(0,500):
		if solve_mat3X3(row,col,sudoku):
			empty_cells-=1
	
		if col < 6:
			row = row
		else:
			row = row+3 if row < 6 else 0	
		col = col+3 if col < 6 else 0
		
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j] == ' ':
				remaining_cells+=1	
	print((remaining_cells/empty_cells)*100, "%")
	return sudoku	
					