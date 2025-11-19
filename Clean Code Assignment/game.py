from Matrix import Matrix
import random


class GoldRush(Matrix):
    
    WINNING_SCORE = 100
    BOARD_ELEMENTS = {"COIN": "$", "WALL": "wall", "EMPTY_CELL": "."}
    
    
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.player1_score = 0 
        self.player2_score = 0
        self.winner_name = "" 
        self.coins_count_on_board = 0


    def is_board_empty(self):
            if self.rows == 0 and self.cols == 0:
                self.board = []
                return True
            return False
        
        
    def initialize_empty_board(self):
        self.board = []
        self.coins_count_on_board = 0
        elements = [self.BOARD_ELEMENTS["COIN"], self.BOARD_ELEMENTS["EMPTY_CELL"], self.BOARD_ELEMENTS["WALL"]]
        return elements
    
    
    def update_random_coins_placed(self, rand_element):
        if rand_element == self.BOARD_ELEMENTS["COIN"]:
            self.coins_count_on_board += 1
            
            
    def fill_odd_rows(self, elements, curr_row):
        rand_index = random.randint(0, 1)  
        rand_element = elements[rand_index]
        self.board[curr_row].append(rand_element)
        
        self.update_random_coins_placed(rand_element)
        
        
    def fill_even_rows(self, curr_row):
        self.board[curr_row].append(self.BOARD_ELEMENTS["WALL"])
                
                
    def replace_walls(self,  elements, curr_row):
            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1 
                rand_index = random.randint(0, 1)
                rand_element = elements[rand_index]
                self.board[curr_row][k] = rand_element
                
                self.update_random_coins_placed(rand_element)
            
                 
    def fill_board(self, elements):
        for i in range(self.rows):
            self.board.append([])
        
            for j in range(self.cols):
                if i % 2 != 0:
                    self.fill_odd_rows(elements, i)
                else:
                    self.fill_even_rows(i)
            if i % 2 == 0:    
                self.replace_walls(elements, i)   
    
    
    def set_players_first_positions(self):
        self.board[0][0] = "player1"
        self.board[self.rows - 1][self.cols - 1] = "player2"
        
        
    def is_board_valid(self):
            return self.coins_count_on_board >= 10


    def load_board(self):
        """
        Initializes the game board with a mix of walls, coins, and empty spaces.
        Ensures at least 10 coins are present on the board.
        """

        if self.is_board_empty() == True:
            return

        elements = self.initialize_empty_board()
        
        self.fill_board(elements)

        self.set_players_first_positions()
        
        if self.is_board_valid() == False:
            return self.load_board()
        else:
            return self.board


    def _is_game_over(self, player):
        player_num = player[-1]
        score = getattr(self, f"player{player_num}_score")
        if score == GoldRush.WINNING_SCORE:
            self.winner_name = player
            return self.winner_name


    def _switch_turns(self, player):
        return "player2" if player == "player1" else "player1"


    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._switch_turns(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.board[new_row][new_col] not in [self.BOARD_ELEMENTS["WALL"], other_player]:
            if self.board[new_row][new_col] == self.BOARD_ELEMENTS["COIN"]:
                self._update_score(player)

            self.board[curr_row][curr_col] = self.BOARD_ELEMENTS["EMPTY_CELL"]
            self.board[new_row][new_col] = player

        return self._is_game_over(player)


    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)


    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)


    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)


    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)


    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)


    def _update_score(self, player):
        player_num = player[-1]
        player_score = f"player{player_num}_score"
        setattr(self, player_score, getattr(self, player_score) + 10)
        print(getattr(self, player_score))




