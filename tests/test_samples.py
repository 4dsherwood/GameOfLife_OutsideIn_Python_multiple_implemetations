import pytest

DEAD = 0
ALIVE = 1
class Game:
    def __init__(self):
        self.oneone = DEAD
    def set_cell_alive(self, x, y):
        self.oneone = ALIVE

    def move_to_next_time(self):
        self.oneone = DEAD

    def get_status(self, x, y):
        if (x==1 and y ==1):
            return self.oneone
        else:
            return DEAD


def create_game_of_life_with_all_dead_cell():
    return Game()


def test_given_living_cell_with_0_live_nieghbors_it_dies():
    # create a game of life
    game = create_game_of_life_with_all_dead_cell()
    # set (1,1) cell to alive
    game.set_cell_alive(1,1)
    assert game.get_status(0, 0) == DEAD
    assert game.get_status(1, 1) == ALIVE
    # move to the next point in time
    game.move_to_next_time()
    # the cell at 1,1 is now dead
    assert game.get_status(1,1) == DEAD
