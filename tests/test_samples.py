from game import Game, DEAD, ALIVE


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


