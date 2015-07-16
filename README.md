# SudokuSatSolver
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/bolinkd/SudokuSatSolver/)
[![Language](https://img.shields.io/badge/language-python-brightgreen.svg)](https://www.python.org/download/releases/2.7/)

Sudoku SAT Solver for CSC320

To run put string encoded sudoku puzzles in a text file and

$ python SSS.py [filename]

Sudoku puzzles must be of form:

`*****6****59*****82****8****45********3********6**3*54***325**6******************`
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



where blank spaces are represented by a wildcard (*.?0 are the acceptable wildcard characters) and digits are the given numbers. 

