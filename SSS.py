import sys


def EveryCellOneNumber():

def EveryNumberOnceInRow():

def EveryNumberOnceInColumn():

def EveryNumberOnceInBox():

def uniqueInteger(xijkList):
	unqiueList = xijkList
	for i in range(0,len(xijkList)):
		uniqueValue = 0
		xijk = xijkList[i]
		if(len(xijk) != 3):
			exit(1)
		uniqueValue += 81*(int(xijk[2])-1)
		uniqueValue += 9*(int(xijk[1])-1)
		uniqueValue += 1*(int(xijk[0])-1)
		unqiueList[i] = uniqueValue+1
	return unqiueList


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
    templist = uniqueInteger(xijk)
    print templist

    EveryCellOneNumber()
    EveryNumberOnceInRow()
    EveryNumberOnceInColumn()
    EveryNumberOnceInBox()



if __name__ == "__main__":
    main()