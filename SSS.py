import glob
import os
import subprocess
import sys
import timeit
import altencode

# How many times to run SAT on each input to get an accurate timing
timer_reps = 5

def convert10to9(hundreds, tens, ones):
	# converts a base 10 number to base 9
	return str(81 * (hundreds-1) + 9 * (tens-1) + ones)

def convert9to10(number):
	# converts a base 9 number [1,729] to base 10
	return (number-1)/81*100+100 + (number-1)%81/9*10+10 + (number-1)%81%9+1

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

def PrintPrettyPuzzle(puzzle):
    # prints a the output variables from SAT prettily!
    for ndx, value in enumerate(puzzle):
    	if ndx%9 == 0 and ndx != 0:
            print
    	if ndx%27 == 0 and ndx != 0:
    		print "-"*6+"+"+"-"*7+"+"+"-"*6
    	if ndx%3 == 0 and ndx%9 != 0:
        	print "|",
        print value%100%10,
    print '\n'

def writeToFile(puzzle, filename, alt=None):
    num_clauses_static = 8343
    if alt:
        with open(filename, "w") as fp:
            altencode.HeaderInfo(fp, len(puzzle[0]) + num_clauses_static)
            altencode.EveryCellOneNumber(fp)
            altencode.EveryNumberOnceInRow(fp)
            altencode.EveryNumberOnceInColumn(fp)
            altencode.EveryNumberOnceInBox(fp)
            fp.write(" 0\n".join(puzzle) + " 0\n")
    else:
        with open(filename, "w") as fp:
            HeaderInfo(fp, len(puzzle[0]) + num_clauses_static)
            EveryCellOneNumber(fp)
            EveryNumberOnceInRow(fp)
            EveryNumberOnceInColumn(fp)
            EveryNumberOnceInBox(fp)
            fp.write(" 0\n".join(puzzle) + " 0\n")

def timeSAT(input_filename, output_filename):
    reps = 500
    setup = """import subprocess; \
        import os; \
        SATinput = '%s'; \
        SAToutput = '%s'; \
        FNULL = open(os.devnull, 'w')
    """ % (input_filename, output_filename)
    return min(timeit.Timer(stmt = """subprocess.call(["./minisat", SATinput, SAToutput], stdout=FNULL)""", setup=setup).repeat(timer_reps, 1))

def main():
    files = glob.glob('./outputs/*')
    for f in files:
        os.remove(f)
    puzzlelist = (x for x in open(sys.argv[1], 'r') if IsValid(x.rstrip()))
    puzzlebools = ((PuzzleToBooleans(x), altencode.PuzzleToBooleans(x)) for x in puzzlelist)
    difference = 0
    for ndx, puzzle in enumerate(puzzlebools):
    	SATinput = 'outputs/' + sys.argv[0] + '.SATinput' + str(ndx) + '.txt'
    	SAToutput = 'outputs/' + sys.argv[0] + '.SAToutput' + str(ndx) + '.txt'
        SATinputalt = 'outputs/' + sys.argv[0] + '.SATinputalt' + str(ndx) + '.txt'
        SAToutputalt = 'outputs/' + sys.argv[0] + '.SAToutputalt' + str(ndx) + '.txt'
        writeToFile(puzzle[0], SATinput)
        writeToFile(puzzle[1], SATinputalt, alt=True)
        
        time_taken = timeSAT(SATinput, SAToutput)
        time_taken_alt = timeSAT(SATinputalt, SAToutputalt)
        difference += time_taken_alt - time_taken
        print "Solution for valid input #" + str(ndx)
        print "Min encoding time: " + str(time_taken)
        print "Alt encoding time: " + str(time_taken_alt)

        result = [convert9to10(int(x)) for x in open(SAToutput, 'r').read().split() if x.isdigit() and int(x) > 0]
        result2 = (result[9*x%81+x/9] for x in xrange(len(result)))
        PrintPrettyPuzzle(result2)
    print "Average difference in minimal and standard encoding: " + str(difference/ndx)

if __name__ == "__main__":
    main()