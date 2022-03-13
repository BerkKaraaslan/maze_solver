from queue import LifoQueue
import sys

def depth_first_search(maze,start_x,start_y):

    stack = LifoQueue()
    visited = []

    start_node = maze[start_y][start_x]

    start_node.is_visited = True
    visited.append(start_node)
    stack.put(start_node)

    while not stack.empty():
        node = stack.get()
        if node.element_type == "E": # we reached the end node
            return maze

        if node.has_right_neighbor():
            rn= node.get_right_neighbor()
            if rn.element_type != "W" and rn not in visited:
                rn.is_visited = True
                visited.append(rn)
                stack.put(rn)

        if node.has_down_neighbor():
            dn= node.get_down_neighbor()
            if dn.element_type != "W" and dn not in visited:
                dn.is_visited = True
                visited.append(dn)
                stack.put(dn)

        if node.has_left_neighbor():
            ln= node.get_left_neighbor()
            if ln.element_type != "W" and ln not in visited:
                ln.is_visited = True
                visited.append(ln)
                stack.put(ln)

        if node.has_up_neighbor():
            un= node.get_up_neighbor()
            if un.element_type != "W" and un not in visited:
                un.is_visited = True
                visited.append(un)
                stack.put(un)

    print("This maze don't have a solution!")
    sys.exit()
    