

class Game:
    def __init__(self):
        def dead_board(x,y):
            print("DEAD")
            return DEAD
        #self.cells = lambda x,y:DEAD
        self.cells = dead_board
    def set_cell_alive(self, x, y):
        old_board = self.cells # takes the lambda function
        def new_board(x1,y1): # closure (aka inner funciton)
            print(f"inner closure for ({x},{y}) called with ({x1},{y1})")
            if x == x1 and y == y1:
                return ALIVE
            else:
                return old_board(x1,y1)
        self.cells = new_board

    def move_to_next_time(self):
        previous = self.cells
        def next_board(x,y):
            count = previous(x-1, y-1) + previous(x-1, y) + previous(x-1, y+1) \
                + previous(x,y-1) + previous(x,y+1) \
                + previous(x+1, y-1) + previous(x+1,y) + previous(x+1, y+1)
            if count == 3 or count == 2 and previous(x,y) == ALIVE:
                return ALIVE
            else:
                return DEAD
        game = Game()
        game.cells = next_board
        return game

    def get_status(self, x, y)-> int:
        return self.cells(x,y)


DEAD: int = 0
ALIVE: int = 1
