import sys
from read_maze import read_maze
from make_maze import make_maze
from solve_maze import solve_maze
from write_solution import write_solution

# traverse sirasiyla sag komsu, alt komsu, sol komsu ve ust komsu seklinde yapilacak

input_file = sys.argv[1] # argv[0] is name of python script
output_file = sys.argv[2]

maze_template = read_maze(input_file) # labirent sablonunu dosyadan okur

maze = make_maze(maze_template) # verilen sablona gore labirenti olusturur

solution_tuple = solve_maze(maze,"a_star_search") # istenilen algoritma ile labirenti cozer

write_solution(solution_tuple,output_file) # cozumu dosyaya yazar