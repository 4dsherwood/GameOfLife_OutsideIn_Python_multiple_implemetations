

class Game:
    def __init__(self):
        # list cells
        # list.get((1,1))
        # lookup of cells
        # lookup.get(1,1)
        self.cells = ""
    def set_cell_alive(self, x, y):
        self.cells += f"({x},{y})"

    def move_to_next_time(self):
        return Game()

    def get_status(self, x, y):
        key = f"({x},{y})"
        return ALIVE if key in self.cells else DEAD


DEAD = 0
ALIVE = 1
