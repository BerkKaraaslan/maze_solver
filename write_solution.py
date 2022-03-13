
def write_solution(solution_tuple,filename):
    with open(filename, "w") as f:

        solution = solution_tuple[0]
        execution_time = solution_tuple[1]
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

        f.write("\n")
        f.write("Execution time is: " + str(execution_time) + " seconds")
        f.close()
    