from Node import Node
import sys
from flood_fill import flood_fill

def make_maze(maze_template):

    clone_maze = []

    for i in range(len(maze_template)):
        line = []
        for j in range(len(maze_template[i])):
            line.append(maze_template[i][j])

        clone_maze.append(line)

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    for i in range(len(maze_template)):
        for j in range(len(maze_template[i])):
            if maze_template[i][j] == "S":
                start_x = j
                start_y = i
            elif maze_template[i][j] == "E":
                end_x = j
                end_y = i

    flood_fill(clone_maze,start_y,start_x)
    if not (clone_maze[start_y][start_x] == "X" and clone_maze[end_y][end_x] == "X"):
        print("This maze don't have a solution!")
        sys.exit()
    
    # orjinal kismin basi
    maze = []

    for i in range(len(maze_template)):
        
        row_items = []
        for j in range(len(maze_template[i])):
            
            node = Node(j,i,maze_template[i][j])
            row_items.append(node)

        maze.append(row_items) 

    row = len(maze)
    col = len(maze[0])

    # x ler saga dogru
    # y ler ise asagi dogru artacak
    
    start_count = 0
    end_count = 0

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            
            if maze[i][j].element_type == "S":
                start_count += 1
            elif maze[i][j].element_type == "E":
                end_count += 1
            elif not (maze[i][j].element_type == "W" or maze[i][j].element_type == "F"):
                print("Bad maze element type! Elements of the maze could only be \"S\", \"E\", \"W\" or \"F\"")
                sys.exit()

            if maze[i][j].x < col - 1: # sag komsu
                maze[i][j].right_neighbor = maze[i][j + 1]

            if maze[i][j].x != 0: # sol komsu
                maze[i][j].left_neighbor = maze[i][j - 1]

            if maze[i][j].y < row - 1: # alt komsu
                maze[i][j].down_neighbor = maze[i + 1][j]

            if maze[i][j].y != 0: # ust komsu
                maze[i][j].up_neighbor = maze[i - 1][j]

    if not (start_count == 1 and end_count == 1):
        print("Bad maze! Maze must have 1 start and 1 exit point!")
        sys.exit()

    return maze