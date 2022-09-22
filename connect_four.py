'''
    B. Lucian Tisdale
    CS5001
    Project
    April 3, 2020

    This program is the driver for connect_four
'''

# connect_four.py
import turtle
import os.path
import random
from grid import Grid
from game import Game, GamePvC


def main():
    print("Welcome to Connect_Four!")
    print("In this version of the game you can choose between player vs. player"
          " mode or player vs. computer. You can also choose the size of the"
          " grid: 6 rows, 7 columns is the default.")
    print()
    num_players = input("Please choose number of players(1 or 2). Press ENTER"
                        " for default of 2(player vs. player): ")
    # while loop insures valid input
    good_player_choice = False
    while good_player_choice == False:
        if num_players == "1" or num_players == "2":
            num_players = int(num_players)
            good_player_choice = True
        elif num_players == "":
            # sets default as 2
            num_players = 2
            good_player_choice = True
        else:
            num_players = input("Enter valid number of players(1 or 2): ")
    num_rows = input("Please enter number of rows(4 through 15). Press ENTER"
                     " for default: ")
    # while loop insures valid input
    good_row_choice = False
    while good_row_choice == False:
        if (num_rows == "4" or num_rows == "5" or num_rows == "6" or
                num_rows == "7" or num_rows == "8" or num_rows == "9" or
                num_rows == "10" or num_rows == "11" or num_rows == "12" or
                num_rows == "13" or num_rows == "14" or num_rows == "15"):
            num_rows = int(num_rows)
            good_row_choice = True
        elif num_rows == "":
            # sets default as 6
            num_rows = 6
            good_row_choice = True
        else:
            num_rows = input("Enter valid number of rows(4 through 15): ")
    num_columns = input("Please enter number of columns(4 through 15). Press"
                        " ENTER for default: ")
    # while loop insures valid input
    good_column_choice = False
    while good_column_choice == False:
        if (num_columns == "4" or num_columns == "5" or num_columns == "6" or 
                num_columns == "7" or num_columns == "8" or
                num_columns == "9" or num_columns == "10" or
                num_columns == "11" or num_columns == "12" or
                num_columns == "13" or num_columns == "14" or
                num_columns == "15"):
            num_columns = int(num_columns)
            good_column_choice = True
        elif num_columns == "":
            # sets default as 7
            num_columns = 7
            good_column_choice = True
        else:
            num_columns = input("Enter valid number of columns(4 through 15): ")

    # setup game
    if num_players == 1:
        g = GamePvC(num_rows, num_columns)
    elif num_players == 2:
        g = Game(num_rows, num_columns)
    g.setup_gameboard()
    # waits for click and passes (x, y) coordinates to get_click
    g.grid.screen.onclick(g.get_click)

    
main()
