from queue import PriorityQueue

def manhattan_distance(src_x,src_y,dest_x,dest_y): # we will use Manhattan Distance as acceptable heuristic values
    return abs(dest_x - src_x) + abs(dest_y - src_y)

def shortest_distance(src_x,src_y,dest_x,dest_y):
    return (dest_x - src_x)**2 + (dest_y - src_y)**2

def greedy_best_first_search(maze,start_x,start_y,end_x,end_y,heuristic):
    
    pq = PriorityQueue()
    start_node = maze[start_y][start_x]
    start_node.is_visited = True
    if heuristic == "manhattan_distance":
        start_node.heuristic_value = manhattan_distance(start_node.x,start_node.y,end_x,end_y)
    elif heuristic == "shortest_distance":
        start_node.heuristic_value = shortest_distance(start_node.x,start_node.y,end_x,end_y)

    start_node.evaluation = start_node.heuristic_value
    pq.put(start_node)

    while not pq.empty():
        node = pq.get()
        
        if node.element_type == "E": # we reached the end node
            return maze

        if node.has_right_neighbor():
            rn= node.get_right_neighbor()
            if rn.element_type != "W":
                rn.is_visited = True
                if heuristic == "manhattan_distance":
                    rn.heuristic_value = manhattan_distance(rn.x,rn.y,end_x,end_y)
                elif heuristic == "shortest_distance":
                    rn.heuristic_value = shortest_distance(rn.x,rn.y,end_x,end_y)
                rn.evaluation = rn.heuristic_value
                pq.put(rn)

        if node.has_down_neighbor():
            dn= node.get_down_neighbor()
            if dn.element_type != "W":
                dn.is_visited = True
                if heuristic == "manhattan_distance":
                    dn.heuristic_value = manhattan_distance(dn.x,dn.y,end_x,end_y)
                elif heuristic == "shortest_distance":
                    dn.heuristic_value = shortest_distance(dn.x,dn.y,end_x,end_y)
                dn.evaluation = dn.heuristic_value
                pq.put(dn)

        if node.has_left_neighbor():
            ln= node.get_left_neighbor()
            if ln.element_type != "W":
                ln.is_visited = True
                if heuristic == "manhattan_distance":
                    ln.heuristic_value = manhattan_distance(ln.x,ln.y,end_x,end_y)
                elif heuristic == "shortest_distance":
                    ln.heuristic_value = shortest_distance(ln.x,ln.y,end_x,end_y)
                ln.evaluation = ln.heuristic_value
                pq.put(ln)

        if node.has_up_neighbor():
            un= node.get_up_neighbor()
            if un.element_type != "W":
                un.is_visited = True
                if heuristic == "manhattan_distance":
                    un.heuristic_value = manhattan_distance(un.x,un.y,end_x,end_y)
                elif heuristic == "shortest_distance":
                    un.heuristic_value = shortest_distance(un.x,un.y,end_x,end_y)
                un.evaluation = un.heuristic_value
                pq.put(un)