def PlacesToNumber(hundreds, tens, ones):
	return str(100*(hundreds) + 10*(tens) + ones)

def HeaderInfo(output, num_clauses):
	output.write("p cnf 999 "+str(num_clauses)+"\n")

def EveryCellOneNumber(output):
    output.write(''.join((str(ndx) + " 0\n" if ndx % 9 == 0 else str(ndx) + " " for ndx in xrange(111, 1000))))

def EveryNumberOnceInRow(output):
    for i in xrange(1, 10):
		for k in xrange(1, 10):
			for j in xrange(1, 9):
				for l in xrange(j + 1, 10):
					output.write("-" + PlacesToNumber(i, j, k) + " -" + PlacesToNumber(i, l, k) + " 0\n")

def EveryNumberOnceInColumn(output):
	for j in xrange(1, 10):
		for k in xrange(1, 10):
			for i in xrange(1, 9):
				for l in xrange(i + 1, 10):
					output.write("-" + PlacesToNumber(i, j, k) + " -" + PlacesToNumber(l, j, k) + " 0\n")

def EveryNumberOnceInBox(output):
	for k in xrange(1, 10):
		for a in xrange(0, 3):
			for b in xrange(0, 3):
				for u in xrange(1, 4):
					for v in xrange(1, 3):
						for w in xrange(v + 1, 3):
							output.write("-" + PlacesToNumber(3*a+u, 3*b+v, k) + " -" + PlacesToNumber(3*a+u, 3*b+w, k) + " 0\n")
	for k in xrange(1, 10):
		for a in xrange(0, 3):
			for b in xrange(0, 3):
				for u in xrange(1, 3):
					for v in xrange(1, 4):
						for w in xrange(u + 1, 4):
							for t in xrange(1, 4):
								output.write("-" + PlacesToNumber(3*a+u, 3*b+v, k) + " -" + PlacesToNumber(3*a+w, 3*b+t, k) + " 0\n")							

def PuzzleToBooleans(puzzle):
	# Converts a puzzle string to a list of variables that must be True for the SAT solver
	return [PlacesToNumber((ndx % 9 + 1), (ndx / 9 + 1), int(char)) for ndx, char in enumerate(puzzle) if char.isdigit() and int(char) != 0]