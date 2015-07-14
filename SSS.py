def printPuzzle(puzzle):
    """takes a string representation of a sudoku puzzle
    and prints it out in pretty format!
    """
    for x in xrange(9):
        if x % 3 == 0 and x != 0:
            print"--"*11
        for y in xrange(9):
            if y % 3 == 0 and y != 0:
                print"|",
            print " " if puzzle[9*x + y] == '*' else puzzle[9*x + y],
        print 

def main():
    prompt = "Input a string representation of a sudoku puzzle!\n\
* is a space and digits are numbers\n\
example: *********************************************************************************\n\
is a fully blank puzzle while\n\
example: 1**3****************************************************************************9\n\
has a 1 in the top corner, a 3 in the fourth column of the first row and a 9 in the bottom right corner\n\
input: "
    puzzle = raw_input(prompt)
    valid_chars = ['0','1','2','3','4','5','6','7','8','9','*']

    if(len(puzzle) != 81):
    	print "Incorrect Puzzle Length" + len(puzzle)
    	exit(1)

    for i in range(0,len(puzzle)):
    	char = puzzle[i]
    	if(char not in valid_chars):
    		print "Incorrect Character " + str(char)
    		exit(1)


    printPuzzle(puzzle)




if __name__ == "__main__":
    main()