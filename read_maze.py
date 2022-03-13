
def read_maze(input_file):
    with open(input_file) as f:
        lines = f.readlines()
        template = []
        for line in lines:
            template.append(line.strip().split(','))

        return template