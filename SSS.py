import sys

def convert10to9(hundreds, tens, ones):
	# converts a base 10 number to base 9
	return str(81 * (hundreds-1) + 9 * (tens-1) + ones)

def HeaderInfo(output, num_clauses):
	output.write("p cnf 729 "+str(num_clauses)+"\n")

def EveryCellOneNumber(output):
    output.write(''.join((str(ndx) + " 0\n" if ndx % 9 == 0 else str(ndx) + " " for ndx in xrange(1, 730))))

def EveryNumberOnceInRow(output):
    for i in xrange(1, 10):
		for k in xrange(1, 10):
			for j in xrange(1, 9):
				for l in xrange(j + 1, 10):
					output.write("-" + convert10to9(i, j, k) + " -" + convert10to9(i, l, k) + " 0\n")

def EveryNumberOnceInColumn(output):
	for j in xrange(1, 10):
		for k in xrange(1, 10):
			for i in xrange(1, 9):
				for l in xrange(i + 1, 10):
					output.write("-" + convert10to9(i, j, k) + " -" + convert10to9(l, j, k) + " 0\n")

def EveryNumberOnceInBox(output):
	for k in xrange(1, 10):
		for a in xrange(0, 3):
			for b in xrange(0, 3):
				for u in xrange(1, 4):
					for v in xrange(1, 3):
						for w in xrange(v + 1, 3):
							output.write("-" + convert10to9(3*a+u, 3*b+v, k) + " -" + convert10to9(3*a+u, 3*b+w, k) + " 0\n")
	for k in xrange(1, 10):
		for a in xrange(0, 3):
			for b in xrange(0, 3):
				for u in xrange(1, 3):
					for v in xrange(1, 4):
						for w in xrange(u + 1, 4):
							for t in xrange(1, 4):
								output.write("-" + convert10to9(3*a+u, 3*b+v, k) + " -" + convert10to9(3*a+w, 3*b+t, k) + " 0\n")							

def PuzzleToBooleans(puzzle):
	# Converts a puzzle string to a list of variables that must be True for the SAT solver
	return [convert10to9((ndx % 9 + 1), (ndx / 9 + 1), int(char)) for ndx, char in enumerate(puzzle) if char.isdigit() and int(char) != 0]

def IsValid(puzzle):
    # takes string representation of a puzzle and returns if it is valid or not
    if(len(puzzle) != 81):
        return False
    valid_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '.', '?', '0'}
    puzzleset = set(puzzle)
    return puzzleset.issubset(valid_chars)

def main():
    puzzlelist = (x for x in open(sys.argv[1], 'r') if IsValid(x.rstrip()))
    puzzlebools = (PuzzleToBooleans(x) for x in puzzlelist)
    num_clauses_static = 8343
    for ndx, puzzle in enumerate(puzzlebools):
        with open("output" + str(ndx) + ".txt", "w") as fp:
            HeaderInfo(fp, len(puzzle) + num_clauses_static)
            EveryCellOneNumber(fp)
            EveryNumberOnceInRow(fp)
            EveryNumberOnceInColumn(fp)
            EveryNumberOnceInBox(fp)
            fp.write(" 0\n".join(puzzle) + " 0\n")

if __name__ == "__main__":
    main()