# Author: Aniebiet Jacob
# Date: 12/1/2018
# Description:
# This program is an algorithmn that finds out the path to how to solve any maze for you


#Constants of which side of a box in the maze is which index in the list of box walls
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3




#This function takes in a maze file and reads in the maze and the returns  dimensions, the end spaces, and all of the other spaces into it creating 3 returns.
# INPUT : maze file
# OUTPUT: maze dimensions, number of rows, number of columns, final row coordinates and final column coordinates
def readMaze(filename):


    list1= []


    stop = 0
    filename = open(filename, "r")


#This for loop goes through the file and takes the first line and takes in list dimensions, takes in the secondline and makes it into coordinates of the end block, and takes in the rest of the boxes of the maze.
    for line in filename:
        if stop == 0:
            row, column = line.strip().split()
            stop = stop + 1
        elif stop == 1:
            rowfinal, colfinal = line.strip().split()
            stop = stop + 1
        else:
            line = line.strip().split()
            list1.append(line)

    filename.close()

    return list1, row, column, rowfinal, colfinal







#This function takes in the list of boxes of the maze and the columns in the maze and utilizes for loops to create and return the finished maze
# INPUT: List of maze boxes, column number
# OUTPUT: finished maze/ 3D list
def makeMaze(list1, column):


    column = int(column)
    rows = []
    maze = []


#This for loop goes through the list of maze-boxes and puts a box in the row for each column in the row. Once the rows length is the same as the number of columns the loop adds that row to the maze and creates a new row.
    for values in range(len(list1)):
        if len(rows) != column:
            rows.append(list1[values])
        if len(rows) == column:
            maze.append(rows)
            rows = []

    return maze







#This function is a recursive function that willuse the user inputed starting coordinates and moze through the maze if there is an open wall (0) in the maze until either it gets to the end of the maze or it realizes there is no end to the maze/ no solution.
# INPUT: the maze, finishing coordinates, starting coordinates and an empty solutions list
# OUTPUT: returns the solution to the maze.
def searchMaze(maze, rowFinal, colFinal, startRow, startColumn, solution):


#This is the recusive base case saying that if the current position is equal to the final position/winning position then return the path
    if startColumn == colFinal and startRow == rowFinal:
        solution.append([rowFinal, colFinal])
        return solution

#This is the second recursive base case that if there is a dead end everywhere the function should return none as a solution
    if maze[startRow][startColumn] == ['1', '1', '1', '1'] or maze[rowFinal][colFinal] == ['1', '1', '1', '1']:
        return None




#This is the recursive case if there is no wall on the right and you haven't just been on the right to then move one column over to the right.
    if maze[startRow][startColumn][RIGHT] == '0' and solution[len(solution)-1] != [startRow,startColumn+1]:
        solution.append([startRow, startColumn])
        return searchMaze(maze, rowFinal, colFinal, startRow, startColumn+1, solution)


#This is the recursive case if there is no wall on the bottom and you haven't just been on the bottom to then move one row over to the bottom.
    elif maze[startRow][startColumn][BOTTOM] == '0' and solution[len(solution)-1] != [startRow+1,startColumn]:
        solution.append([startRow, startColumn])
        return searchMaze(maze, rowFinal, colFinal, startRow+1, startColumn, solution)


#This is the recursive case if there is no wall on the left and you haven't just been on the left to then move one column back to the left.
    elif maze[startRow][startColumn][LEFT] == '0' and solution[len(solution)-1] != [startRow,startColumn-1]:
        solution.append([startRow, startColumn])
        return searchMaze(maze, rowFinal, colFinal, startRow, startColumn-1, solution)


#This is the recursive case if there is no wall on the top and you haven't just been on the top to then move one row back to the top.
    elif maze[startRow][startColumn][TOP] == '0' and solution[len(solution)-1] != [startRow-1,startColumn]:
        solution.append([startRow, startColumn])
        return searchMaze(maze, rowFinal, colFinal, startRow-1, startColumn, solution)




#This is the final recursive case that if the function gets to a dead end where no walls are open it closes that part of the maze off so it doesn't go back there and goes back over to the box it previously was in to look for new open walls
    else:
        row = solution[len(solution)-1][0]
        column = solution[len(solution)-1][1]


#If cases say that depending on current position of the maze, it will close up both walls (wall of current box and wall of last box) it just came through
        if row > startRow:
            maze[startRow][startColumn][BOTTOM] = '1'
            maze[row][column][TOP] = '1'
        elif row < startRow:
            maze[startRow][startColumn][TOP] = '1'
            maze[row][column][BOTTOM] = '1'
        elif column > startColumn:
            maze[startRow][startColumn][RIGHT] = '1'
            maze[row][column][LEFT] = '1'
        elif column < startColumn:
            maze[startRow][startColumn][LEFT] = '1'
            maze[row][column][RIGHT] = '1'

        startRow = row
        startColumn = column

        solution.remove(solution[len(solution)-1])
        return searchMaze(maze, rowFinal, colFinal, startRow, startColumn, solution)





#This is the main funtion and it takes in no parameter but it uses all of the previously made functions and impliments them.
def main():



    print("Welcome to the Maze Solver!")
    theFile = input("Pleases enter the name of the file with the maze: ")

    list1, row, column, rowFinal, colFinal = readMaze(theFile)
    maze = makeMaze(list1, column)

    rowFinal = int(rowFinal)
    colFinal = int(colFinal)




    startRow = int(input("Please enter a starting row: "))

#While loop ensures that user enters a valid row number and if not promtes the user to do so.
    while startRow < 0 or startRow > rowFinal:
        startRow = int(input("Invalid number, please enter a value between 0 and "+str(rowFinal)+" inclusive: "))



    startColumn = int(input("Please enter a starting column: "))

#While loop ensures that user enters a valid column number and if not promtes the user to do so.
    while startColumn < 0 or startColumn > colFinal:
        startColumn = int(input("Invalid number, please enter a value between 0 and "+str(colFinal)+" inclusive: "))





#This creates an empty list outside of our searchMaze function and puts in starting coordinates so list index is always in range.
    result = []
    result.append([startRow,startColumn])
    solutions  = searchMaze(maze, rowFinal, colFinal, startRow, startColumn, result)




#Statement that ensures if the searchMaze function returns None that the program reports that no solutions were found.
    if solutions == None:
        print("No solutions found!")

    else:
        print("SOLUTION FOUND!")

#This for loop prints each coordinate of the path to the end of the maze on its own line
        for space in range(1, len(solutions)):
            print(solutions[space])


main()
