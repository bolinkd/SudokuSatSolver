def printPuzzle(puzzle):
	"""takes a string representation of a sudoku puzzle
	and prints it out 
	"""
	pass

def main():
    prompt = "Input a string representation of a sudoku puzzle!\n\
* is a space and digits are numbers\n\
example: *********************************************************************************\n\
is a fully blank puzzle while\n\
example: 1**3****************************************************************************9\n\
has a 1 in the top corner, a 3 in the fourth column of the first row and a 9 in the bottom right corner\n\
input: "
    puzzle = input(prompt)


if __name__ == "__main__":
	main()