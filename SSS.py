import sys

def HeaderInfo(output, num_clauses):
	output.write("p cnf 729 "+str(num_clauses)+"\n")

def EveryCellOneNumber(output):
	pass

def EveryNumberOnceInRow(output):
	pass

def EveryNumberOnceInColumn(output):
	pass

def EveryNumberOnceInBox(output):
	pass

def PuzzleToBooleans(puzzle):
	"""
	Converts a puzzle to a list of variables that must be True for the SAT solver
	"""
	return [81*(ndx%9) + 9*(ndx/9) + int(char) for ndx, char in enumerate(puzzle) if char.isdigit()]

def PrettifyPuzzle(puzzle):
    """
    takes a string representation of a sudoku puzzle and prints it out in pretty format!
    """
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

def IsValid(puzzle):
    """ 
    takes string representation of a puzzle and returns if it is valid or not
    """
    if(len(puzzle) != 81):
        return False
    valid_chars = {'0','1','2','3','4','5','6','7','8','9','*'}
    puzzleset = set(puzzle)
    return puzzleset.issubset(valid_chars)

def main():
    puzzlelist = (x for x in open(sys.argv[1], 'r') if IsValid(x.rstrip()))
    # print "\n".join([PrettifyPuzzle(x) for x in puzzlelist])
    puzzlebools = (PuzzleToBooleans(x) for x in puzzlelist)
    # print "\n".join([str(x) for x in puzzlebools])
    
    num_clauses_static = 2835
    for ndx, puzzle in enumerate(puzzlebools):
        with open("output"+str(ndx)+".txt", "w") as fp:
            HeaderInfo(fp, len(puzzle) + num_clauses_static)
            EveryCellOneNumber(fp)
            EveryNumberOnceInRow(fp)
            EveryNumberOnceInColumn(fp)
            EveryNumberOnceInBox(fp)
            for expr in puzzle:
                fp.write(str(expr) + " 0\n")


if __name__ == "__main__":
    main()