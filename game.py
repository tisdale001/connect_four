'''
    B. Lucian Tisdale
    CS5001
    Project
    April 3, 2020

    This program contains classes Game and GamePvC for connect_four.py
'''
# game.py
import turtle
import os.path
import random
from grid import Grid

class Game():
    ''' class: Game
        Attributes: grid (creates a new instance of Grid), game_list (creates
            a new game_list of "0's" representing empty spaces), row_num_list,
            num_rows, num_columns, red_score, yel_score (yellow score),
            player ("R" or "Y"), color ("red" or "yellow"), winner (Boolean)
        Methods:
            setup_gameboard (draws gameboard)
            populate_game_list (creates game_list with "O's")
            update_game_list (adds "R" or "Y" to appropriate place in game)
            create_row_num_list (creates list of empty columns as 0's)
            update_row_num_list (adds 1 to appropriate column in row_num_list)
            get_row (returns row number of player move)
            get_column (returns column number player clicked on)
            get_click (main function that runs after onclick)
            switch_player (returns opposite player str)
            get_color (returns color of current player)
            column_win (checks for column win of most recent move)
            row_win (checks for row win of most recent move)
            forward_slash_diag (checks for diagonal win of most recent move)
            back_slash_diag (checks for other diagonal win of most recent move)
            board_full (checks if board is full, resulting in a tie)
            fill_all_columns (fills row_num_list so no more clicks are possible)
            write_score_to_file (writes winner's score to .txt file)
    '''

    def __init__(self, num_rows, num_columns):
        ''' Constructor -- creates a new instance of Game
            Parameters: self (the current object), number of rows,
                        number of columns
        '''
        self.grid = Grid(num_rows, num_columns)
        self.game_list = self.populate_game_list(num_rows, num_columns)
        self.row_num_list = self.create_row_num_list(num_rows, num_columns)
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.red_score = self.grid.initialize_red_score("red_score.txt")
        self.yel_score = self.grid.initialize_yel_score("yellow_score.txt")
        self.player = "R"
        self.color = "red"
        self.winner = False
    def setup_gameboard(self):
        ''' Method: setup_gameboard (calls Grid methods for setup)
            Parameters: self (the current object)
            Returns: void
        '''
        # setup all turtles
        self.grid.p.hideturtle()
        self.grid.q.hideturtle()
        self.grid.r.hideturtle()
        self.grid.t.hideturtle()
        self.grid.p.speed(0)
        self.grid.q.speed(0)
        self.grid.r.speed(0)
        self.grid.t.speed(0)
        self.grid.t.up()
        # set turtle t in position for blue rectangle
        self.grid.t.setposition((self.grid.pos_x - self.grid.radius -
                        self.grid.grid_width * 2),(self.grid.pos_y -
                        self.grid.grid_width * 2))
        self.grid.draw_rectangle(self.grid.t, "blue")
        self.grid.draw_white_circles(self.grid.t, "white")
        self.grid.draw_arrows(self.grid.t, "black")
        # set turtle r in position for printing score
        self.grid.r.up()
        self.grid.r.setposition(0, self.grid.pos_y + self.grid.num_rows *
                                self.grid.row_width + self.grid.radius * 3)
        self.grid.draw_score(self.grid.r, self.red_score, self.yel_score)
        # draws player and color left of gameboard
        self.grid.draw_player(self.grid.q, self.grid.p, self.player, self.color)
    def populate_game_list(self, num_rows, num_columns):
        ''' Method: populate_game_list (creates game_list)
            Parameters:
                self -- the current object
                num_rows -- number of rows (int)
                num_columns -- number of columns (int)
            Returns: game_list (nested list)
        '''
        game_list = []
        for i in range(num_columns):
            row_list = []
            for j in range(num_rows):
                row_list.append("O")
            game_list.append(row_list)
        return game_list
    def update_game_list(self, game_list, row, column, player):
        ''' Method: update_game_list (updates game_list with player's move)
            Parameters:
                self -- the current object
                game_list -- nested list
                row -- row number of player's move (int)
                column -- column number of player's move (int)
                player -- current player name, "R" or "Y" (str)
            Returns: void
        '''
        game_list[column - 1][row - 1] = player
    def create_row_num_list(self, num_rows, num_columns):
        ''' Method: create_row_num_list (creates row_num_list)
            Parameters:
                self -- the current object
                num_rows -- number of rows
                num_columns -- number of columns
            Returns: row_num_list (list)
        '''
        row_num_list = []
        for i in range(num_columns):
            row_num_list.append(0)
        return row_num_list
    def update_row_num_list(self, row_num_list, column):
        ''' Method: update_row_num_list (adds one to appropriate column)
            Parameters:
                self -- the current object
                row_num_list -- list
                column -- column number that a piece was added to (int)
            Returns: void
        '''
        row_num_list[column - 1] += 1
    def get_row(self, row_num_list, column):
        ''' Method: get_row (returns row number of last play)
            Parameters:
                self -- the current object
                row_num_list -- list
                column -- column number of last play (int)
            Return:  row number of last play (int)
        '''
        return row_num_list[column - 1]
    def get_column(self, x, y):
        ''' Method: get_column (returns column number clicked on)
            Parameters: self (the current object), x coordinate, y coordinate
            Returns: number of column clicked or "50" if not valid click (int)
        '''
        lower_x_limit = (self.grid.pos_x - self.grid.radius -
                         self.grid.grid_width * 2)
        upper_x_limit = (self.grid.pos_x + self.grid.radius +
                         self.grid.grid_width)
        lower_y_limit = (self.grid.pos_y - self.grid.grid_width * 2)
        upper_y_limit = (self.grid.pos_y + self.grid.row_width *
                         self.num_rows + self.grid.radius * 2)
        # if statements return column number clicked
        for i in range(self.num_columns):
            if (lower_x_limit + self.grid.column_width * i < x < upper_x_limit
                + self.grid.column_width * i and lower_y_limit < y <
                upper_y_limit):
                return i + 1
        # returns high number 50 to show that no column was clicked
        return 50

    def get_click(self, x, y):
        ''' Method: get_click (gets click from onclick and runs the rest of
                    the program)
            Parameters: self (current object), x coordinate, y coordinate
            Returns: void
        '''
        column = self.get_column(x, y)
        # if/else statement decides if column is valid and runs rest of program
        if (column <= self.num_columns) and (self.row_num_list[column - 1]
                            < self.num_rows):
            self.update_row_num_list(self.row_num_list, column)
            row = self.get_row(self.row_num_list, column)
            self.update_game_list(self.game_list, row, column, self.player)
            # sets position and draws circle of player move
            self.grid.t.setposition(self.grid.pos_x + self.grid.column_width *
                    (column - 1), self.grid.pos_y + self.grid.row_width *
                                    (row - 1))
            self.grid.draw_circle(self.grid.t, self.color)
            
            # check for win
            if (self.column_win(column, self.num_rows, self.player) or
                    self.row_win(row, self.num_columns, self.player) or
                    self.forward_slash_diag(row, column, self.player) or
                    self.back_slash_diag(row, column, self.player)):
                self.winner = True
                # fills all columns in list so no more clicks will be valid
                self.row_num_list = self.fill_all_columns(self.row_num_list)
                # following clears screen and draws black winner screen
                self.grid.t.clear()
                self.grid.r.clear()
                self.grid.q.clear()
                self.grid.p.clear()
                self.grid.screen.bgcolor("black")
                self.grid.t.setposition(0, 0)
                self.grid.t.color("white")
                self.grid.t.write("The winner is: " + self.color, align =
                                  "center", font = ("Arial", 48, "normal"))
                # writes winner score to .txt file
                if self.player == "R":
                    self.red_score += 1
                elif self.player == "Y":
                    self.yel_score += 1
                self.write_score_to_file(self.player)

            # checks if board is full       
            elif self.board_full(self.game_list):
                self.winner = True
                # clears screen and draws black "tie" screen
                self.grid.t.clear()
                self.grid.r.clear()
                self.grid.q.clear()
                self.grid.p.clear()
                self.grid.screen.bgcolor("black")
                self.grid.t.setposition(0, 0)
                self.grid.t.color("white")
                self.grid.t.write("The game is a tie", align =
                                  "center", font = ("Arial", 48, "normal"))
            # if statement checks if game is over    
            if self.winner == False:
                # switch player and color
                self.player = self.switch_player(self.player)
                self.color = self.get_color(self.player)
                # draws new player
                self.grid.draw_player(self.grid.q, self.grid.p, self.player,
                                  self.color)
        else:
            # dummy command in case click is invalid (not a column)
            click = "nothing"

    def switch_player(self, player):
        ''' Method: switch_player (returns opposite player)
            Parameters: self (the current object), player -- "R" or "Y" (str)
            Returns: "R" or "Y" (str)
        '''
        if player == "R":
            return "Y"
        elif player == "Y":
            return "R"
    def get_color(self, player):
        ''' Method: get_color (returns color string)
            Parameters: self (the current object), player -- "R" or "Y" (str)
            Returns: "red" or "yellow" (str)
        '''
        if player == "R":
            return "red"
        if player == "Y":
            return "yellow"
    def column_win(self, start_point_column, num_rows, player):
        ''' Method: column_win (checks for column win)
            Parameters:
                self -- the current object
                start_point_column -- column number of last play (int)
                num_rows -- number of rows (int)
                player -- "R" or "Y" (str)
            Returns: Boolean
        '''
        test_str = ''
        player_str = ''
        # creates test_str
        for i in range(num_rows):
            test_str += self.game_list[start_point_column - 1][i]
        # creates player_str, either "RRRR" or "YYYY"
        for i in range(4):
            player_str += player
        # checks if player_str(four-in-a-row) is in test_str
        if player_str in test_str:
            return True
        else:
            return False
    def row_win(self, start_point_row, num_columns, player):
        ''' Method: row_win (checks if row is a win)
            Parameters:
                self -- the current object
                start_point_row -- row number of last play (int)
                num_columns -- number of columns (int)
                player -- "R" or "Y" (str)
            Returns: Boolean
        '''
        test_str = ''
        player_str = ''
        # creates test_str
        for i in range(num_columns):
            test_str += self.game_list[i][start_point_row - 1]
        # creates player_str, either "RRRR" or "YYYY"
        for i in range(4):
            player_str += player
        # checks if player_str(four-in-a-row) is in test_str
        if player_str in test_str:
            return True
        else:
            return False
    def forward_slash_diag(self, start_point_row, start_point_column, player):
        ''' Method: forward_slash_diag (checks for forward slash diagonal win)
            Parameters:
                self -- the current object
                start_point_row -- row number of last play (int)
                start_point_column -- column number of last play (int)
                player -- "R" or "Y" (str)
            Returns: Boolean
        '''
        left_row = start_point_row
        left_column = start_point_column
        # while statement finds leftmost position of diagonal
        while left_row > 1 and left_column > 1:
            left_row -= 1
            left_column -= 1
        right_row = start_point_row
        right_column = start_point_column
        # while statement finds rightmost position of diagonal
        while right_row < self.num_rows and right_column < self.num_columns:
            right_row += 1
            right_column += 1
        test_str = ''
        player_str = ''
        # creates test_str using diagonal limits of board
        while left_row <= right_row and left_column <= right_column:
            test_str += self.game_list[left_column - 1][left_row - 1]
            left_row += 1
            left_column += 1
        # creates player_str, either "RRRR" or "YYYY"
        for i in range(4):
            player_str += player
        # checks if player_str(four-in-a-row) is in test_str
        if player_str in test_str:
            return True
        else:
            return False
    def back_slash_diag(self, start_point_row, start_point_column, player):
        ''' Method: back_slash_diag (checks for back slash diagonal win)
            Parameters:
                self -- the current object
                start_point_row -- row number of last play (int)
                start_point_column -- column number of last play (int)
                player -- "R" or "Y" (str)
            Returns: Boolean
        '''
        left_row = start_point_row
        left_column = start_point_column
        # while statement finds leftmost position of diagonal
        while left_row < self.num_rows and left_column > 1:
            left_row += 1
            left_column -= 1
        right_row = start_point_row
        right_column = start_point_column
        # while statement finds rightmost position of diagonal
        while right_row > 1 and right_column < self.num_columns:
            right_row -= 1
            right_column += 1
        test_str = ''
        player_str = ''
        # creates test_str using diagonal limits of board
        while left_row >= right_row and left_column <= right_column:
            test_str += self.game_list[left_column - 1][left_row - 1]
            left_row -= 1
            left_column += 1
        # creates player_str, either "RRRR" or "YYYY"
        for i in range(4):
            player_str += player
        # checks if player_str(four-in-a-row) is in test_str
        if player_str in test_str:
            return True
        else:
            return False
    def board_full(self, game_list):
        ''' Method: board_full (checks if gameboard is full)
            Parameters: self -- the current object, game_list (nested list)
            Returns: Boolean
        '''
        # checks if any placeholders("O") are in game_list
        for i in game_list:
            if "O" in i:
                return False
        return True
    def fill_all_columns(self, row_num_list):
        ''' Method: fill_all_columns (creates max value for all columns)
            Parameters: self -- the current object, row_num_list (list of ints)
            Returns: row_num_list (list)
        '''
        # ends the game by making no more clicks valid
        for i in range(self.num_columns):
            row_num_list[i] = self.num_rows
        return row_num_list
    def write_score_to_file(self, player):
        ''' Method: write_score_to_file (writes player score to .txt file)
            Parameters:
                self -- the current object
                player -- "R" or "Y" (str)
            Returns: void
        '''
        if player == "R":
            try:
                with open('red_score.txt', 'w') as outfile:
                    outfile.write(str(self.red_score))
            except OSError:
                print("Could not save score.")
        elif player == "Y":
            try:
                with open('yellow_score.txt', 'w') as outfile:
                    outfile.write(str(self.red_score))
            except OSError:
                print("Could not save score.")
        else:
            print("Could not save score.")

class GamePvC(Game):
    ''' class: GamePvC (player vs. computer, a subclass of Game)
        Attributes: grid (creates a new instance of Grid), game_list (creates
            a new game_list of "0's" representing empty spaces), row_num_list,
            num_rows, num_columns, red_score, yel_score (yellow score),
            player ("R" or "Y"), color ("red" or "yellow"), winner (Boolean)
        Methods:
            write_score_to_file (writes winning player score to .txt file)
            get_click (gets coordinates from onclick and runs rest of program)
            The rest of the methods are borrowed from Game class.
    '''
    def __init__(self, num_rows, num_columns):
        ''' Constructor -- creates a new instance of Grid
            Parameters:
                self -- the current object
                num_rows -- number of rows (int)
                num_columns -- number of columns (int)
        '''
        self.grid = Grid(num_rows, num_columns)
        self.game_list = self.populate_game_list(num_rows, num_columns)
        self.row_num_list = self.create_row_num_list(num_rows, num_columns)
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.red_score = self.grid.initialize_red_score("red_score2.txt")
        self.yel_score = self.grid.initialize_yel_score("yellow_score2.txt")
        self.player = "R"
        self.color = "red"
        self.winner = False
    def write_score_to_file(self, player):
        ''' Method: write_score_to_file (writes winning player score to
                                            .txt file)
            Parameters: self -- the current object, player -- "R" or "Y" (str)
            Returns: void
        '''
        if player == "R":
            try:
                with open('red_score2.txt', 'w') as outfile:
                    outfile.write(str(self.red_score))
            except OSError:
                print("Could not save score.")
        elif player == "Y":
            try:
                with open('yellow_score2.txt', 'w') as outfile:
                    outfile.write(str(self.red_score))
            except OSError:
                print("Could not save score.")
        else:
            print("Could not save score.")
    def get_click(self, x, y):
        ''' Method: get_click (gets (x, y) coordinates from onclick and
                                runs rest of program)
            Parameters: self -- the current object, x coordinate, y coordinate
            Returns: void
        '''
        column = self.get_column(x, y)
        # checks if column is valid
        if (column <= self.num_columns) and (self.row_num_list[column - 1]
                            < self.num_rows):
            self.update_row_num_list(self.row_num_list, column)
            row = self.get_row(self.row_num_list, column)
            self.update_game_list(self.game_list, row, column, self.player)
            # sets position of t turtle and draws piece on gameboard
            self.grid.t.setposition(self.grid.pos_x + self.grid.column_width *
                    (column - 1), self.grid.pos_y + self.grid.row_width *
                                    (row - 1))
            self.grid.draw_circle(self.grid.t, self.color)
            
            # check for win
            if (self.column_win(column, self.num_rows, self.player) or
                    self.row_win(row, self.num_columns, self.player) or
                    self.forward_slash_diag(row, column, self.player) or
                    self.back_slash_diag(row, column, self.player)):
                self.winner = True
                # fills rows to maximum to make future clicks invalid
                self.row_num_list = self.fill_all_columns(self.row_num_list)
                # clears screen and creates black "win" screen
                self.grid.t.clear()
                self.grid.r.clear()
                self.grid.q.clear()
                self.grid.p.clear()
                self.grid.screen.bgcolor("black")
                self.grid.t.setposition(0, 0)
                self.grid.t.color("white")
                self.grid.t.write("The winner is: " + self.color, align =
                                  "center", font = ("Arial", 48, "normal"))
                # writes new red score to .txt file
                self.red_score += 1
                self.write_score_to_file(self.player)
            # elif statement checks if gameboard is full
            elif self.board_full(self.game_list):
                self.winner = True
                # clears screen and creates black "tie" screen
                self.grid.t.clear()
                self.grid.r.clear()
                self.grid.q.clear()
                self.grid.p.clear()
                self.grid.screen.bgcolor("black")
                self.grid.t.setposition(0, 0)
                self.grid.t.color("white")
                self.grid.t.write("The game is a tie", align =
                                  "center", font = ("Arial", 48, "normal"))
            # checks if game is over
            if self.winner == False:
                # switch player and color
                self.player = self.switch_player(self.player)
                self.color = self.get_color(self.player)
                self.grid.draw_player(self.grid.q, self.grid.p, self.player,
                                  self.color)
                # begin computer turn
                good_choice = False
                # while loop insures computer choice is valid
                while good_choice == False:
                    column = random.randint(1, self.num_columns)
                    if self.row_num_list[column - 1] < self.num_rows:
                        good_choice = True
                self.update_row_num_list(self.row_num_list, column)
                row = self.get_row(self.row_num_list, column)
                self.update_game_list(self.game_list, row, column, self.player)
                # sets position of t turtle and draws game piece on gameboard
                self.grid.t.setposition(self.grid.pos_x + self.grid.column_width
                                        * (column - 1), self.grid.pos_y +
                                        self.grid.row_width * (row - 1))
                self.grid.draw_circle(self.grid.t, self.color)
                # check for computer win
                if (self.column_win(column, self.num_rows, self.player) or
                        self.row_win(row, self.num_columns, self.player) or
                        self.forward_slash_diag(row, column, self.player) or
                        self.back_slash_diag(row, column, self.player)):
                    self.winner = True
                    # fills rows so future clicks are invalid
                    self.row_num_list = self.fill_all_columns(self.row_num_list)
                    # clears screen and draws black "win" screen
                    self.grid.t.clear()
                    self.grid.r.clear()
                    self.grid.q.clear()
                    self.grid.p.clear()
                    self.grid.screen.bgcolor("black")
                    self.grid.t.setposition(0, 0)
                    self.grid.t.color("white")
                    self.grid.t.write("The winner is: " + self.color, align =
                                  "center", font = ("Arial", 48, "normal"))
                    # writes yellow score to .txt file
                    self.yel_score += 1
                    self.write_score_to_file(self.player)
                # checks if gameboard is full
                elif self.board_full(self.game_list):
                    self.winner = True
                    # clears screen and draws black "tie" screen
                    self.grid.t.clear()
                    self.grid.r.clear()
                    self.grid.q.clear()
                    self.grid.p.clear()
                    self.grid.screen.bgcolor("black")
                    self.grid.t.setposition(0, 0)
                    self.grid.t.color("white")
                    self.grid.t.write("The game is a tie", align =
                                  "center", font = ("Arial", 48, "normal"))
                # if statement checks if game is over
                if self.winner == False:
                    # switch player and color
                    self.player = self.switch_player(self.player)
                    self.color = self.get_color(self.player)
                    self.grid.draw_player(self.grid.q, self.grid.p,
                                          self.player, self.color)
        else:
            # dummy command in case player clicks outside of range
            click = "nothing"

