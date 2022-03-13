import queue
import sys

def breadth_first_search(maze,start_x,start_y):
    
    q = queue.Queue()
    visited = []

    start_node = maze[start_y][start_x]

    start_node.is_visited = True
    visited.append(start_node)
    q.put(start_node)

    while not q.empty():
        node = q.get()
        if node.element_type == "E": # we reached the end node
            return maze

        if node.has_right_neighbor():
            rn= node.get_right_neighbor()
            if rn.element_type != "W" and rn not in visited:
                rn.is_visited = True
                visited.append(rn)
                q.put(rn)

        if node.has_down_neighbor():
            dn= node.get_down_neighbor()
            if dn.element_type != "W" and dn not in visited:
                dn.is_visited = True
                visited.append(dn)
                q.put(dn)

        if node.has_left_neighbor():
            ln= node.get_left_neighbor()
            if ln.element_type != "W" and ln not in visited:
                ln.is_visited = True
                visited.append(ln)
                q.put(ln)

        if node.has_up_neighbor():
            un= node.get_up_neighbor()
            if un.element_type != "W" and un not in visited:
                un.is_visited = True
                visited.append(un)
                q.put(un)

    print("This maze don't have a solution!")
    sys.exit()