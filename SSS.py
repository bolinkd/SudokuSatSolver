import sys

def uniqueInteger(value):
	returnValue = 0
	if(len(value) != 3):
		exit(1)
	for i in range(0,len(value)):
		if(i == 0):
			returnValue += 81*(int(value[0])-1)
		if(i == 1):
			returnValue += 9*(int(value[0])-1)
		if(i == 2):
			returnValue += 1*(int(value[0])-1)

	return returnValue+1


def xijkString(puzzle):
	"""
	Takes a puzzle string and puts it
	into Xijk format
	"""
	result = ""
	for i in range(0,len(puzzle)):
		char = puzzle[i]
		column = i%9+1
		row = i/9 + 1
		if(char != '*'):
			info = str(column) + str(row) + char + ','
			result += info
	return result[0:-1]

def printPuzzle(index, puzzle):
    """takes a string representation of a sudoku puzzle
    and prints it out in pretty format!
    """
    print "Puzzle " + str(index+1)
    for x in xrange(9):
        if x % 3 == 0 and x != 0:
            print"--"*11
        for y in xrange(9):
            if y % 3 == 0 and y != 0:
                print"|",
            print " " if puzzle[9*x + y] == '*' else puzzle[9*x + y],
        print 
    print 
    return puzzle.rstrip()

def isValid(puzzle):
    """ takes string representation of a puzzle and
    returns if it is valid or not
    """
    if(len(puzzle) != 81):
        return False
    valid_chars = {'0','1','2','3','4','5','6','7','8','9','*'}
    puzzleset = set(puzzle)
    return puzzleset.issubset(valid_chars)

def main():
    puzzlelist = [printPuzzle(ndx, x) for ndx,x in enumerate(open(sys.argv[1], 'r')) if isValid(x.rstrip())]
    xijkList = xijkString(puzzlelist[3])
    xijk = xijkList.split(',')
    print xijk
    for value in xijk:
    	temp = uniqueInteger(value)
        print temp,


if __name__ == "__main__":
    main()