
def write_solution(solution,filename):
    with open(filename, "w") as f:

        for i in range(len(solution)):

            row = ""
            for j in range(len(solution[i])):

                if solution[i][j].is_visited is True and solution[i][j].element_type != "S" and solution[i][j].element_type != "E":
                    row = row + "X"
                else:
                    row = row + solution[i][j].element_type

                if j != len(solution[i]) - 1:
                    row = row + ","


            f.write(row + "\n")


        f.close()
    