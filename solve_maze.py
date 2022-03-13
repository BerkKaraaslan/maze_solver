from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from a_star_search import a_star_search
from greedy_best_first_search import greedy_best_first_search
import time

def solve_maze(maze,algorithm):

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j].element_type == "S": # start node u
                start_x = j
                start_y = i
            elif maze[i][j].element_type == "E": # end node u
                end_x = j
                end_y = i

    start_time = time.time()

    if algorithm == "breadth_first_search":
        solution = breadth_first_search(maze,start_x,start_y)
    elif algorithm == "depth_first_search":
        solution = depth_first_search(maze,start_x,start_y)
    elif algorithm == "a_star_search":
        solution = a_star_search(maze,start_x,start_y,end_x,end_y,"shortest_distance")
    elif algorithm == "greedy_best_first_search":
        solution = greedy_best_first_search(maze,start_x,start_y,end_x,end_y,"shortest_distance")

    end_time = time.time()
    return (solution, end_time - start_time)