'''
    B. Lucian Tisdale
    CS5001
    Project
    April 4, 2020

    This is test code for connect_four.
'''

# test_connect_four.py
from grid import Grid
from game import Game, GamePvC
import unittest

class GridTest(unittest.TestCase):
    def test_init(self):
        grid = Grid(6, 7)
        self.assertEqual(grid.num_rows, 6)
        self.assertEqual(grid.num_columns, 7)
        self.assertEqual(grid.radius, 20)
        self.assertEqual(grid.row_width, 48)
        self.assertEqual(grid.column_width, 48)
        self.assertEqual(grid.grid_width, 4)
        self.assertEqual(grid.pos_x, -168)
        self.assertEqual(grid.pos_y, -144)

        grid2 = Grid(4, 5)
        self.assertEqual(grid2.num_rows, 4)
        self.assertEqual(grid2.num_columns, 5)
        self.assertEqual(grid2.radius, 20)
        self.assertEqual(grid2.row_width, 48)
        self.assertEqual(grid2.column_width, 48)
        self.assertEqual(grid2.grid_width, 4)
        self.assertEqual(grid2.pos_x, -120)
        self.assertEqual(grid2.pos_y, -96)

    def test_initialize_red_score(self):
        grid = Grid(6, 7)
        self.assertEqual(grid.initialize_red_score('nofile.txt'), 0)

    def test_initialize_yel_score(self):
        grid = Grid(6, 7)
        self.assertEqual(grid.initialize_yel_score('nofile.txt'), 0)

class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game(3, 4)
        self.assertEqual(game.grid.num_rows, 3)
        self.assertEqual(game.grid.num_columns, 4)
        self.assertEqual(game.game_list, [["O", "O", "O"],
                                          ["O", "O", "O"],
                                          ["O", "O", "O"],
                                          ["O", "O", "O"]])
        self.assertEqual(game.row_num_list, [0, 0, 0, 0])
        self.assertEqual(game.num_rows, 3)
        self.assertEqual(game.num_columns, 4)
        self.assertEqual(game.player, "R")
        self.assertEqual(game.color, "red")
        self.assertEqual(game.winner, False)

    def test_populate_game_list(self):
        game = Game(4, 6)
        self.assertEqual(game.populate_game_list(game.num_rows,
                                game.num_columns), [["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"]])

    def test_update_game_list(self):
        game = Game(3, 4)
        game.update_game_list(game.game_list, 1, 1, "R")
        self.assertEqual(game.game_list, [["R", "O", "O"], ["O", "O", "O"],
                                          ["O", "O", "O"], ["O", "O", "O"]])
        game.update_game_list(game.game_list, 2, 2, "Y")
        self.assertEqual(game.game_list, [["R", "O", "O"], ["O", "Y", "O"],
                                          ["O", "O", "O"], ["O", "O", "O"]])

    def test_create_row_num_list(self):
        game = Game(3, 4)
        self.assertEqual(game.create_row_num_list(3, 4), [0, 0, 0, 0])
        self.assertEqual(game.create_row_num_list(4, 5), [0, 0, 0, 0, 0])

    def test_update_row_num_list(self):
        game = Game(3, 4)
        game.update_row_num_list(game.row_num_list, 1)
        self.assertEqual(game.row_num_list, [1, 0, 0, 0])
        game.update_row_num_list(game.row_num_list, 1)
        self.assertEqual(game.row_num_list, [2, 0, 0, 0])
        game.update_row_num_list(game.row_num_list, 2)
        self.assertEqual(game.row_num_list, [2, 1, 0, 0])

    def test_get_row(self):
        game = Game(5, 6)
        self.assertEqual(game.get_row([5, 4, 3, 2, 1, 0], 1), 5)
        self.assertEqual(game.get_row([5, 4, 3, 2, 1, 0], 2), 4)
        self.assertEqual(game.get_row([5, 4, 3, 2, 1, 0], 3), 3)
        self.assertEqual(game.get_row([5, 4, 3, 2, 1, 0], 4), 2)

    def test_switch_player(self):
        game = Game(9, 10)
        self.assertEqual(game.switch_player("R"), "Y")
        self.assertEqual(game.switch_player("Y"), "R")

    def test_get_color(self):
        game = Game(10, 10)
        self.assertEqual(game.get_color("R"), "red")
        self.assertEqual(game.get_color("Y"), "yellow")

    def test_column_win(self):
        game = Game(4, 4)
        self.assertEqual(game.column_win(4, 4, "R"), False)
        game.game_list = [["O", "O", "O", "O"], ["O", "O", "O", "O"],
                          ["O", "O", "O", "O"], ["R", "R", "R", "R"]]
        self.assertEqual(game.column_win(4, 4, "R"), True)

    def test_row_win(self):
        game = Game(4, 4)
        self.assertEqual(game.row_win(1, 4, "R"), False)
        game.game_list = [["R", "O", "O", "O"], ["R", "O", "O", "O"],
                          ["R", "O", "O", "O"], ["R", "O", "O", "O"]]
        self.assertEqual(game.row_win(1, 4, "R"), True)

    def test_forward_slash_diag(self):
        game = Game(4, 4)
        self.assertEqual(game.forward_slash_diag(1, 1, "R"), False)
        game.game_list = [["R", "O", "O", "O"], ["O", "R", "O", "O"],
                          ["O", "O", "R", "O"], ["O", "O", "O", "R"]]
        self.assertEqual(game.forward_slash_diag(1, 1, "R"), True)

    def test_back_slash_diag(self):
        game = Game(4, 4)
        self.assertEqual(game.back_slash_diag(4, 1, "R"), False)
        game.game_list = [["0", "O", "O", "R"], ["O", "O", "R", "O"],
                          ["O", "R", "O", "O"], ["R", "O", "O", "O"]]
        self.assertEqual(game.back_slash_diag(4, 1, "R"), True)

    def test_board_full(self):
        game = Game(4, 4)
        self.assertEqual(game.board_full(game.game_list), False)
        game.game_list = [["Y", "R", "Y", "R"], ["Y", "R", "R", "Y"],
                          ["R", "R", "Y", "Y"], ["R", "Y", "R", "Y"]]
        self.assertEqual(game.board_full(game.game_list), True)

    def test_fill_all_columns(self):
        game = Game(6, 7)
        self.assertEqual(game.fill_all_columns(game.row_num_list),
                         [6, 6, 6, 6, 6, 6, 6])
        game2 = Game(7, 8)
        self.assertEqual(game2.fill_all_columns(game2.row_num_list),
                         [7, 7, 7, 7, 7, 7, 7, 7])

    def test_write_score_to_file(self):
        game = Game(6, 7)
        game.red_score = 1
        game.yel_score = 1
        game.write_score_to_file("R")
        game.write_score_to_file("Y")

        game2 = Game(7, 8)
        self.assertEqual(game2.red_score, 1)
        self.assertEqual(game2.yel_score, 1)

class TestGamePvC(unittest.TestCase):
    def test_init(self):
        game = GamePvC(3, 4)
        self.assertEqual(game.grid.num_rows, 3)
        self.assertEqual(game.grid.num_columns, 4)
        self.assertEqual(game.game_list, [["O", "O", "O"],
                                          ["O", "O", "O"],
                                          ["O", "O", "O"],
                                          ["O", "O", "O"]])
        self.assertEqual(game.row_num_list, [0, 0, 0, 0])
        self.assertEqual(game.num_rows, 3)
        self.assertEqual(game.num_columns, 4)
        self.assertEqual(game.player, "R")
        self.assertEqual(game.color, "red")
        self.assertEqual(game.winner, False)

    def test_write_score_to_file(self):
        game = GamePvC(6, 7)
        game.red_score = 1
        game.yel_score = 1
        game.write_score_to_file("R")
        game.write_score_to_file("Y")

        game2 = Game(7, 8)
        self.assertEqual(game2.red_score, 1)
        self.assertEqual(game2.yel_score, 1)

    def test_populate_game_list(self):
        # testing one method in Parent class Game
        game = GamePvC(4, 6)
        self.assertEqual(game.populate_game_list(game.num_rows,
                                game.num_columns), [["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"],
                                                   ["O", "O", "O", "O"]])
        

def main():
    unittest.main(verbosity = 3)

main()
