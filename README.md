# SudokuSatSolver
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/bolinkd/SudokuSatSolver/)
[![Language](https://img.shields.io/badge/language-python-brightgreen.svg)](https://www.python.org/download/releases/2.7/)

Sudoku SAT Solver for CSC320

To run put string encoded sudoku puzzles in a text file and

$ python SSS.py [filename]

Sudoku puzzles must be of form:

`*****6****59*****82****8****45********3********6**3*54***325**6******************`

is the same as:
```
      |     6 |
  5 9 |       |    8
2     |     8 |
--------------------
  4 5 |       |
    3 |       |
    6 |     3 |  5 4
--------------------
      | 3 2 5 |    6
      |       |
      |       |
```

where blank spaces are represented by a wildcard (*.?0 are the acceptable wildcard characters) and digits are the given numbers. The program will run the text files through minisat in order to get a solution and then post that to the console for the user to copy down. The text files for intermediate points can be found as listed below.

The CNF texts are availble upon completion of running the program by looking in the outputs file,
	The input file for the puzzle is the file that is put into the SATSolver
	The output file for the puzzle is the file that is returned from the SATSolver

To run the 16x16 verson oof the program use the command below:

$ python SSS16.py [filename]

Sudoku puzzle of the form:
```
g*b**2**9*6a********4e*378**g**fdf****6*****c1e*c***a**7*1*********6*c*58**g**a**dc*b****426****e9*g***a*f*d*b**8*4**fed***c**7****d**b2*g19***3**8*3*f**b****5e6***9****d****1**g*bc**e*6f*8***5*6f**9**c**3*g*2****a*c**5*e8**3*a**7*g*e*8dc4*****f*2**9**7**6
```

the encoding must follow the rules of the following dictionary (notice 0 is not used as it is used also as a blank space holder):
HexToDec = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16}

will return a completed puzzle of the form:
```
g e b 3 | 1 2 c f | 9 5 6 a | 4 7 d 8 
a 5 1 2 | 4 e d 3 | 7 8 c b | g 6 9 f 
d f 7 8 | 5 b 6 9 | g 2 4 3 | c 1 e a 
c 6 9 4 | a 8 g 7 | e 1 d f | 5 2 3 b 
--------------------------------------
b 3 f 6 | 2 c 4 5 | 8 7 e g | 1 9 a d 
7 d c a | b 9 3 1 | 5 4 2 6 | f e 8 g 
e 9 5 g | 7 6 8 a | 1 f 3 d | 2 b c 4 
8 2 4 1 | g f e d | b a 9 c | 6 3 7 5 
--------------------------------------
f 7 e d | 8 5 b 2 | c g 1 9 | a 4 6 3 
1 4 8 c | 3 d f 6 | 2 b a 7 | 9 g 5 e 
6 a 2 5 | 9 g 7 4 | 3 d 8 e | b f 1 c 
9 g 3 b | c 1 a e | 4 6 f 5 | 8 d 2 7 
--------------------------------------
5 8 6 f | e 4 9 b | d c 7 2 | 3 a g 1 
2 b g 7 | d a 1 c | 6 3 5 4 | e 8 f 9 
3 1 a 9 | 6 7 5 g | f e b 8 | d c 4 2 
4 c d e | f 3 2 8 | a 9 g 1 | 7 5 b 6 
```

Sample inputs for the 9x9 Solver can be found in: sample.txt
A Sample input for the 16x16 Solver can be found in: sample16.txt
