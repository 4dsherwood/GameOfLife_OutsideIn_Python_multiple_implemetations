import pytest

DEAD = 0
ALIVE = 1
class Game:
    def __init__(self):
        # list cells
        # list.get((1,1))
        # lookup of cells
        # lookup.get(1,1)
        self.cells = []  # list of tuples
    def set_cell_alive(self, x, y):
        self.cells.append((x,y))

    def move_to_next_time(self):
        return Game()

    def get_status(self, x, y):
        key = (x,y)
        if key in self.cells:
            return ALIVE
        else:
            return DEAD


def create_game_of_life_with_all_dead_cell():
    return Game()


def test_given_living_cell_with_0_live_nieghbors_it_dies():
    game = create_game_of_life_with_all_dead_cell()
    game.set_cell_alive(1,1)
    assert game.get_status(0, 0) == DEAD
    assert game.get_status(1, 1) == ALIVE
    game = game.move_to_next_time()
    assert game.get_status(1,1) == DEAD


def test_0_0_is_alive():
    game = create_game_of_life_with_all_dead_cell()
    game.set_cell_alive(0,0)
    assert game.get_status(0, 0) == ALIVE


