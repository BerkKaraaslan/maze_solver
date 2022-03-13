
class Node:

    right_neighbor = None
    down_neighbor = None
    left_neighbor = None
    up_neighbor = None
    
    def __init__(self,x,y,element_type,is_visited = False):
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.element_type =element_type # type of this node for ex: "E" means exit
        self.is_visited = is_visited # initially not visited
        # daha sonra buraya heuristic degeri 
        # gercek masrafi vs de ekle !!!

    def __str__(self): # objeyi print edebilmek icin
        return f"Type: {self.element_type} x = {self.x} y = {self.y} is visited = {self.is_visited}"

    def __repr__(self): # objeyi print edebilmek icin
        return f"Type: {self.element_type} x = {self.x} y = {self.y} is visited = {self.is_visited}"
        
    def get_right_neighbor(self):
        return self.right_neighbor

    def get_down_neighbor(self):
        return self.down_neighbor

    def get_left_neighbor(self):
        return self.left_neighbor

    def get_up_neighbor(self):
        return self.up_neighbor

    def has_right_neighbor(self):
        if self.right_neighbor is None:
            return False
        else: 
            return True

    def has_down_neighbor(self):
        if self.down_neighbor is None:
            return False
        else: 
            return True

    def has_left_neighbor(self):
        if self.left_neighbor is None:
            return False
        else: 
            return True

    def has_up_neighbor(self):
        if self.up_neighbor is None:
            return False
        else: 
            return True

    