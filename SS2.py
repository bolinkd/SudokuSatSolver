import sys

def PrettifyPuzzle(puzzle):
    # takes a string representation of a sudoku puzzle and prints it out in pretty format!
    pretty_puzzle = ""
    for x in xrange(9):
        if x % 3 == 0 and x != 0:
            pretty_puzzle += "--"*11 + "\n"
        for y in xrange(9):
            if y % 3 == 0 and y != 0:
                pretty_puzzle += "| "
            pretty_puzzle += "  " if puzzle[9*x + y] == '*' else puzzle[9*x + y]+" "
        pretty_puzzle += "\n"
    return pretty_puzzle


def main():
	fp = open(sys.argv[1], 'r')
	result = []
	values =  fp.read().split()
	for value in values:
		if value.isdigit():
			if int(value) > 0:
				result.append(int(value))
	if(len(result) == 81):
		pass

	# result = [x for x in open(sys.argv[1], 'r').read().split() if int(value) > 0]

	for ndx, value in enumerate(result):
		value = value - 1
		i = value/81+1
		value = value%81
		j = value/9+1
		value = value%9
		k = value+1
		result[ndx] = str(i) + str(j) + str(k)
	print result
	puzzle = ""
	for number in result:
		puzzle += number[2];
	print puzzle
	print PrettifyPuzzle(puzzle)







if __name__ == "__main__":
    main()