import sys

from read_maze import read_maze
from make_maze import make_maze
from solve_maze import solve_maze
from write_solution import write_solution

# depth first breath first  a star greedy best first search (maybe)

# a star da heuristic olarak o noktanin cikis noktasina olan Manhattan Distance i kullanilacak

# btutun traverse ler arrayde 4 KOMSULUK a gore bakilarak yapilacak

# traverse un yonu ise sag komsudan baslayip saat yonunde gidecek

# yani
# 1) sag komsu
# 2) alt komsu
# 3) sol komsu
# 4) ust komsu

# labirent 2d array olarak yapilacak

# node diye bir class olacak
# objeler buradan uretilecek
# node un type ı (free,exit vs) , x ve y koordinatlari, visit edilip edilmedigi vs objede tutulabilir

# ONEMLİ  !!!! cozum olmayan durumlarda visited listesine eklemeye devam eder ve her durumda onun buyuklugunu kontrol eder
# eger visited listesi labirentin buyuklugunden yani (len(maze) * len(maze[0]) ifadesinden buyuk ise cozum yok diye doner


input_file = sys.argv[1] # argv[0] is name of python script
output_file = sys.argv[2]

maze_template = read_maze(input_file) # dosyadan labirenti okuyup istenen formatta bize donecek dondugu sey 2D karakter arrayi olacak

maze = make_maze(maze_template) # template i alip 2D obje arrayini gerekli bilgilerle olusturup donecek

solution = solve_maze(maze,"depth_first_search") # istenen algo ile cozup cozumu don

write_solution(solution,output_file) # cozumu parametre olan dosyaya yazar
