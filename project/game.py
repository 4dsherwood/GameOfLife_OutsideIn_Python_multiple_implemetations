

class Game:
    def __init__(self):
        def dead_board(x,y):
            return DEAD
        #self.cells = lambda x,y:DEAD
        self.cells = dead_board
    def set_cell_alive(self, x, y):
        old_board = self.cells # takes the lambda function
        def new_board(x1,y1): # closure (aka inner funciton)
            if x == x1 and y == y1:
                return ALIVE
            else:
                return old_board(x,y)
        self.cells = new_board

    def move_to_next_time(self):
        return Game()

    def get_status(self, x, y)-> int:
        return self.cells(x,y)


DEAD: int = 0
ALIVE: int = 1
