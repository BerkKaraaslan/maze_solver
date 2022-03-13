from Node import Node

def make_maze(maze_template):

    maze = []

    for i in range(len(maze_template)):
        
        row_items = []
        for j in range(len(maze_template[i])):
            
            node = Node(j,i,maze_template[i][j])
            row_items.append(node)

        maze.append(row_items) 

    # komsular atanacak
    row = len(maze) # bu sayi satirin limit olacak yani en buyuk satir sayisi = row - 1
    col = len(maze[0]) # bu sayi sutunun limiti olacak yani en buyuk sutun sayisi = col - 1
    # maze dikdortgen olacagi icin col = maze[0] diyebildik

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            
            # sag komsu sadece x degeri ile ilgili 
            # x i 1 fazla varsa sag komsusu vardir
            if maze[i][j].x < col - 1:
                maze[i][j].right_neighbor = maze[i][j + 1]

            if maze[i][j].x != 0: # sol komsu
                maze[i][j].left_neighbor = maze[i][j - 1]

            if maze[i][j].y < row - 1: # alt komsu
                maze[i][j].down_neighbor = maze[i + 1][j]

            if maze[i][j].y != 0: # ust komsu
                maze[i][j].up_neighbor = maze[i - 1][j]

        
    return maze

# x saga dogru artacak
# en soldakilerin x degeri 0, en sagdakilerin x degeri ise col - 1

# y asagi dogru artacak
# en usttekilerin y degeri 0, en asagidakilerin y degeri sie row - 1
