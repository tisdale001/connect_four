'''
    B. Lucian Tisdale
    CS5001
    Project
    April 3, 2020

    This program contains Grid class for connect_four.py
'''

# grid.py
import turtle
import os.path
import random

class Grid():
    ''' class: Grid
        Attributes: num_rows, num_columns, radius, row_width, column_width,
            grid_width, screen (turtle screen), (t, r, q, p) -- turtle names,
            pos_x (x coordinate), pos_y (y coordinate) -- lower left starting
            positions
        Methods:
            draw_rectangle (draws blue rectangle for gameboard)
            draw_circle (draws one circle given color)
            draw_white_circles (draws white circles on gameboard)
            draw_arrows (draws black arrows above gameboard)
            initialize_red_score (reads score from file)
            initialize_yel_score (reads score from file)
            draw_score (writes scores above gameboard)
            draw_player (draws player color left of gameboard)
    '''
    def __init__(self, num_rows, num_columns):
        ''' Constructor -- creates a new instance of Grid
            Parameters: self (the current object), number or rows,
                number of columns
        '''
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.radius = 20
        self.row_width = 40 + 8
        self.column_width = 40 + 8
        self.grid_width = 4
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()
        self.r = turtle.Turtle()
        self.q = turtle.Turtle()
        self.p = turtle.Turtle()
        self.pos_x = (self.column_width * num_columns // -2)
        self.pos_y = (self.row_width * num_rows // -2)
    def draw_rectangle(self, turtle_name, color):
        ''' Method: draw_rectangle
            Parameters:
                self -- the current object
                turtle_name -- name of turtle object
                color -- (intended to be blue)
            Returns: void
        '''
        turtle_name.left(90)
        turtle_name.down()
        turtle_name.color(color)
        turtle_name.begin_fill()
        for i in range(2):
            turtle_name.forward(self.row_width * self.num_rows +
                                self.grid_width * 2)
            turtle_name.right(90)
            turtle_name.forward(self.column_width * self.num_columns +
                                self.grid_width * 2)
            turtle_name.right(90)
        turtle_name.right(90)
        turtle_name.end_fill()
        turtle_name.up()
    def draw_circle(self, turtle_name, color):
        ''' Method: draw_circle (draws one circle)
            Parameters:
                self -- the current object
                turtle_name -- name of turtle object
                color -- (intended to be red, yellow, or white)
            Returns: void
        '''
        turtle_name.color(color)
        turtle_name.down()
        turtle_name.begin_fill()
        turtle_name.circle(self.radius)
        turtle_name.end_fill()
        turtle_name.up()
    def draw_white_circles(self, turtle_name, color):
        ''' Method: draw_white_circles (fills gameboard with white circles)
            Parameters:
                self -- the current object
                turtle_name -- name of turtle object
                color -- (intended to be white)
            Returns: void
        '''
        turtle_name.color(color)
        column = 0
        while column < self.num_columns:
            row = 0
            while row < self.num_rows:
                turtle_name.setposition((self.pos_x + self.column_width *
                            column), (self.pos_y + self.row_width * row))
                self.draw_circle(turtle_name, color)
                row += 1
            column += 1
    def draw_arrows(self, turtle_name, color):
        ''' Method: draw_arrows (draws black pointer arrows above gameboard)
            Parameters:
                self -- the current object
                turtle_name -- name of turtle object
                color -- (intended to be black)
            Returns: void
        '''
        turtle_name.color(color)
        row = 0
        column = 0
        # while loop draws same number of arrows as columns
        while column < self.num_columns:
            turtle_name.setposition(self.pos_x + self.column_width * column,
                                self.pos_y + self.num_rows * self.row_width +
                                self.radius)
            turtle_name.begin_fill()
            turtle_name.down()
            turtle_name.left(120)
            turtle_name.forward(10)
            turtle_name.right(120)
            turtle_name.forward(10)
            turtle_name.right(120)
            turtle_name.forward(10)
            turtle_name.left(120)
            turtle_name.up()
            turtle_name.end_fill()
            column += 1
    def initialize_red_score(self, score_file):
        ''' Method: initialize_red_score (reads red score from file)
            Parameters:
                self -- the current object
                score_file -- .txt file which contains string of integer
            Returns: red score or 0 (int)
        '''
        if os.path.exists(score_file):
            try:
                with open(score_file, 'r') as infile:
                    return int(infile.read())
            except OSError:
                print("Could not load score.")
                return 0
        else:
            return 0
    def initialize_yel_score(self, score_file):
        ''' Method: initialize_yel_score (reads yellow score from file)
            Parameters:
                self -- the current object
                score_file -- .txt file which contains string of integer
            Returns: yellow score or 0 (int)
        '''
        if os.path.exists(score_file):
            try:
                with open(score_file, 'r') as infile:
                    return int(infile.read())
            except OSError:
                print("Could not load score.")
                return 0
        else:
            return 0
    def draw_score(self, turtle_name, red_score, yel_score):
        ''' Method: draw_score (writes scores above gameboard)
            Parameters:
                self -- the current object
                turtle_name -- name of turtle object
                red_score -- int
                yel_score -- int
            Returns: void
        '''
        turtle_name.write("red: " + str(red_score) + "    yellow: " +
                          str(yel_score), align = "center", font =
                          ("Arial", 16, "normal"))
    def draw_player(self, turtle1, turtle2, player, color):
        ''' Method: draw_player (draws colored circle and player name left
                    of gameboard)
            Parameters:
                self -- the current object
                turtle1 -- name of turtle object
                turtle2 -- name of turtle object
                player -- str ("R" or "Y")
                color -- str ("red" or "yellow")
            Returns: void
        '''
        turtle1.clear()
        turtle2.clear()
        turtle1.speed(0)
        turtle2.speed(0)
        turtle1.up()
        turtle2.up()
        turtle1.setposition(self.pos_x - self.column_width * 2, 0)
        self.draw_circle(turtle1, color)
        turtle2.setposition(self.pos_x - self.column_width * 2,
                            self.row_width * (-1) - self.radius)
        if player == "R":
            turtle2.write("Red's \nturn!", align = "center", font =
                            ("Arial", 16, "normal"))
        elif player == "Y":
            turtle2.write("Yellow's \nturn!", align = "center", font =
                            ("Arial", 16, "normal"))
        
