from approvaltests import verify

from game import Game, DEAD, ALIVE


def create_game_of_life_with_all_dead_cell():
    return Game()


def test_given_living_cell_with_0_live_nieghbors_it_dies():
    game = create_game_of_life_with_all_dead_cell()
    game.set_cell_alive(1, 1)
    assert game.get_status(0, 0) == DEAD
    assert game.get_status(1, 1) == ALIVE
    game = game.move_to_next_time()
    assert game.get_status(1, 1) == DEAD


def test_0_0_is_alive():
    game = create_game_of_life_with_all_dead_cell()
    game.set_cell_alive(0, 0)
    assert game.get_status(0, 0) == ALIVE


def test_blinker():
    game = create_game_of_life_with_all_dead_cell()
    game.set_cell_alive(2, 1)
    game.set_cell_alive(3, 1)
    game.set_cell_alive(4, 1)
    game.set_cell_alive(1, 2)
    game.set_cell_alive(2, 2)
    game.set_cell_alive(3, 2)
    story_board = ""
    story_board += str(game) + "\n"
    assert game.get_status(2, 2) == ALIVE
    assert game.get_status(5, 6) == DEAD
    step1 = game.move_to_next_time()
    story_board += str(step1)

    step2 = step1.move_to_next_time()
    assert step1.get_status(1, 2) == ALIVE
    assert step2.get_status(2,1) == ALIVE
    verify(story_board)
