
def flood_fill(maze,x,y):
    
    if maze[x][y] == "S" or maze[x][y] == "F" or maze[x][y] == "E":  
        maze[x][y] = "X" 
        
        if y < len(maze[0]) - 1: # sag komsu
            flood_fill(maze, x,y + 1)

        if y > 0: # sol komsu
            flood_fill(maze, x,y - 1)
        
        if x > 0: # yukari komsu
            flood_fill(maze,x - 1, y)

        if x < len(maze) - 1: # asagi komsu
            flood_fill(maze,x + 1, y)

    # x satir
    # y ise sutun olarak gelecek
    # x asagi dogru artacak
    # y ise saga dogru artacak