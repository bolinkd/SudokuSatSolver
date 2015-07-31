import glob
import os
import subprocess
import sys

HexToDec = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16}
DecToHex = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'a','11':'b','12':'c','13':'d','14':'e','15':'f','16':'g'}
    

def convert10to16(hundreds, tens, ones):
	# converts a base 10 number to base 9
	return str(256 * (hundreds-1) + 16 * (tens-1) + ones)

def convert16to10(number):
	# converts a base 9 number [1,729] to base 10
	i = ((number-1)/256*100+100)/100
	#print 'i: ' + str(i)
	j = ((number-1)%256/16*10+10)/10
	#print 'j: ' + str(j)
	k = (number-1)%256%16+1
	#print 'k: ' + DecToHex[str(k)]
	return {'i':i, 'j':j, 'k':DecToHex[str(k)]}

def HeaderInfo(output, num_clauses):
	output.write("p cnf 4096 "+str(num_clauses)+"\n")

def EveryCellOneNumber(output):
    output.write(''.join((str(ndx) + " 0\n" if ndx % 16 == 0 else str(ndx) + " " for ndx in xrange(1, 4097))))

def EveryNumberOnceInRow(output):
    for i in xrange(1, 17):
		for k in xrange(1, 17):
			for j in xrange(1, 16):
				for l in xrange(j + 1, 17):
					output.write("-" + convert10to16(i, j, k) + " -" + convert10to16(i, l, k) + " 0\n")

def EveryNumberOnceInColumn(output):
	for j in xrange(1, 17):
		for k in xrange(1, 17):
			for i in xrange(1, 16):
				for l in xrange(i + 1, 17):
					output.write("-" + convert10to16(i, j, k) + " -" + convert10to16(l, j, k) + " 0\n")

def EveryNumberOnceInBox(output):
	for k in xrange(1, 17):
		for a in xrange(0, 4):
			for b in xrange(0, 4):
				for u in xrange(1, 5):
					for v in xrange(1, 4):
						for w in xrange(v + 1, 4):
							output.write("-" + convert10to16(4*a+u, 4*b+v, k) + " -" + convert10to16(4*a+u, 4*b+w, k) + " 0\n")
	for k in xrange(1, 17):
		for a in xrange(0, 4):
			for b in xrange(0, 4):
				for u in xrange(1, 4):
					for v in xrange(1, 5):
						for w in xrange(u + 1, 5):
							for t in xrange(1, 5):
								output.write("-" + convert10to16(4*a+u, 4*b+v, k) + " -" + convert10to16(4*a+w, 4*b+t, k) + " 0\n")							

def PuzzleToBooleans(puzzle):
	# Converts a puzzle string to a list of variables that must be True for the SAT solver
	rtn = []
	for ndx, char in enumerate(puzzle):
		if char in HexToDec.keys():
			val = convert10to16(ndx % 16 + 1, ndx / 16 + 1, HexToDec[char])
			rtn.append(val)
	return rtn

def IsValid(puzzle):
    # takes string representation of a puzzle and returns if it is valid or not
    if(len(puzzle) != 256):
    	print "OPPS"
        return False
    valid_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b' ,'c', 'd', 'e', 'f', 'g', '*', '.', '?', '0'}
    puzzleset = set(puzzle)
    return puzzleset.issubset(valid_chars)

def PrintPrettyPuzzle(puzzle):
    # prints a the output variables from SAT prettily!
    for ndx, value in enumerate(puzzle):
    	if ndx%16 == 0 and ndx != 0:
            print
    	if ndx%(16*4) == 0 and ndx != 0:
    		print "-"*38
    	if ndx%4 == 0 and ndx%16 != 0:
        	print "|",
        print value%100%10,
    print '\n'

def main():
    files = glob.glob('./outputs/*')
    for f in files:
        os.remove(f)
    puzzlelist = (x for x in open(sys.argv[1], 'r') if IsValid(x.rstrip()))
    puzzlebools = (PuzzleToBooleans(x) for x in puzzlelist)
    num_clauses_static = 89344
    for ndx, puzzle in enumerate(puzzlebools):
    	filename = 'outputs/' + sys.argv[0] + '.SATinput' + str(ndx) + '.txt'
    	filename2 = 'outputs/' + sys.argv[0] + '.SAToutput' + str(ndx) + '.txt'
        with open(filename, "w") as fp:
            HeaderInfo(fp, len(puzzle) + num_clauses_static)
            EveryCellOneNumber(fp)
            EveryNumberOnceInRow(fp)
            EveryNumberOnceInColumn(fp)
            EveryNumberOnceInBox(fp)
            fp.write(" 0\n".join(puzzle) + " 0\n")
        with open(os.devnull, 'w') as FNULL:
            subprocess.call(["./minisat", filename, filename2], stdout=FNULL)
#        for x in open(filename2, 'r').read().split():
#            if x.isdigit() and int(x) > 0:
#        	    i,j,k = convert16to10(int(x)) 
#        	    print 'i: ' + str(i) + ' j: ' + str(j) + ' k: ' + k
        result = [convert16to10(int(x)) for x in open(filename2, 'r').read().split() if x.isdigit() and int(x) > 0]
        icount = 0
    	for i in xrange(1,17):
    		jcount = 0
    		print ''
    		if icount %4 == 0 and icount != 0:
    			print ('-'*38)
    		icount = icount + 1
    		for j in xrange(1,17):
    			if jcount%4 == 0 and jcount != 0:
    				print '|',
    			jcount = jcount + 1
    			for k in xrange(0,256):
    				if result[k]['i'] == j:
    					if result[k]['j'] == i:
    						print result[k]['k'],
    	print ''
    		

if __name__ == "__main__":
    main()
