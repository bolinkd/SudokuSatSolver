import sys


def RuleToBooleans(rules):
	result = rules
	for ndx, item in enumerate(rules):
		result[ndx] = 81*(int(item[0])-1) + 9*(int(item[1])-1) + (int(item[2])-1) + 1 
	return result

def HeaderInfo(output, num_clauses):
	output.write("p cnf 729 "+str(num_clauses)+"\n")

def EveryCellOneNumber(output):
	for i in range(1,10):
		for j in range(1,10):
			rule = []
			for k in range(1,10):
				rule.append(str(i)+str(j)+str(k))
			printable = ""
			for boolean in RuleToBooleans(rule):
				printable += str(boolean) + " "
			output.write(printable + "0\n")



def EveryNumberOnceInRow(output):
	for i in range(1,10):
		for k in range(1,10):
			for j in range(1,9):
				for l in range(j+1, 10):
					rule = []
					rule.append(str(i)+str(j)+str(k))
					rule.append(str(i)+str(l)+str(k))
					printable = ""
					for boolean in RuleToBooleans(rule):
						printable += "-" + str(boolean) + " "
					output.write(printable + "0\n")

def EveryNumberOnceInColumn(output):
	for j in range(1,10):
		for k in range(1,10):
			for i in range(1,9):
				for l in range(i+1, 10):
					rule = []
					rule.append(str(i)+str(j)+str(k))
					rule.append(str(l)+str(j)+str(k))
					printable = ""
					for boolean in RuleToBooleans(rule):
						printable += "-" + str(boolean) + " "
					output.write(printable + "0\n")

def EveryNumberOnceInBox(output):
	for k in range(1,10):
		for a in range(0,3):
			for b in range(0,3):
				for u in range(1,4):
					for v in range(1,3):
						for w in range(v+1,3):
							rule = []
							rule.append(str(3*a+u)+str(3*b+v)+str(k))
							rule.append(str(3*a+u)+str(3*b+w)+str(k))
							printable = ""
							for boolean in RuleToBooleans(rule):
								printable += "-" + str(boolean) + " "
							output.write(printable + "0\n")
	for k in range(1,10):
		for a in range(0,3):
			for b in range(0,3):
				for u in range(1,3):
					for v in range(1,4):
						for w in range(u+1,4):
							for t in range(1,4):
								rule = []
								rule.append(str(3*a+u)+str(3*b+v)+str(k))
								rule.append(str(3*a+w)+str(3*b+t)+str(k))
								printable = ""
								for boolean in RuleToBooleans(rule):
									printable += "-" + str(boolean) + " "
								output.write(printable + "0\n")


							

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
    
    num_clauses_static = 8343
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