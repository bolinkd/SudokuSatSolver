import sys



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
    [printPuzzle(ndx, x) for ndx,x in enumerate(open(sys.argv[1], 'r')) if isValid(x.rstrip())]


if __name__ == "__main__":
    main()