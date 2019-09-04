'''
CSC263 Winter 2019
Problem Set 4 Starter Code
University of Toronto Mississauga
'''
# Do NOT add any "import" statements

class Square:
  def __init__(self, row, column, sub_ways=None):
    self.row = row
    self.column = column
    self.sub_ways = sub_ways
  

class Game:
  def __init__(self, dan_chess, sushant_chess, nrow, ncols):
    self.dan_chess = dan_chess # dan_chess
    self.sushant_chess = sushant_chess
    self.nrow = nrow
    self.ncols = ncols
    self.num_dan_moves = 0
    self.num_sushant_moves = 0
    
  def sushant_next_moves(self,square):
    '''
    return a list of valid move
    '''
    all_possible_des = []
    
    #Case 1: 1 up, 2 right
    if square.row + 1 <= self.nrow -1 and square.column + 2 <= self.ncols - 1:
      square_des1 = Square(square.row + 1, square.column + 2)
      all_possible_des.append(square_des1)
      
    #Case 2: 1 up, 2 left
    if square.row + 1 <= self.nrow - 1 and square.column - 2 >= 0:
      square_des2 = Square(square.row + 1, square.column - 2)
      all_possible_des.append(square_des2)
      
    #Case 3: 1 down, 2 right
    if square.row - 1 >= 0 and square.column + 2 <= self.ncols - 1:
      square_des3 = Square(square.row - 1, square.column + 2)
      all_possible_des.append(square_des3)
      
    #Case 4: 1 down, 2 left
    if square.row - 1 >= 0 and square.column - 2 >= 0:
      square_des4 = Square(square.row - 1, square.column - 2)
      all_possible_des.append(square_des4)
      
    #Case 5: 2 up, 1 right
    if square.row + 2 <= self.nrow -1 and square.column + 1 <= self.ncols-1:
      square_des5 = Square(square.row + 2, square.column + 1)
      all_possible_des.append(square_des5)
      
    #Case 6: 2 up, 1 left
    if square.row + 2 <= self.nrow -1 and square.column - 1 >= 0:
      square_des6 = Square(square.row + 2, square.column - 1)
      all_possible_des.append(square_des6)
      
    #Case 7: 2 down, 1 right
    if square.row - 2 >= 0 and square.column + 1 <= self.ncols-1:
      square_des7 = Square(square.row - 2, square.column + 1)
      all_possible_des.append(square_des7)
      
    #Case 8: 2 down, 1 left
    if square.row - 2 >= 0 and square.column -1 >= 0:
      square_des8 = Square(square.row - 2, square.column - 1)
      all_possible_des.append(square_des8)
      
    return all_possible_des

  def get_number_2(self,x_distance, y_distance):
    return 2*(x_distance) - y_distance

  def get_number_1(self,x_distance, y_distance):
    return x_distance - 2*self.get_number_2(x_distance, y_distance)
  
  def check_s_valid(self, square):
    if square.row < self.nrow-1 and square.column > 0 and square.column < self.ncolumn -1:
      return True
    return False
  
  def check_if_dan_win_directly(self):
    number_dan_win_moves = self.nrow - self.dan_chess.row-1
    dan_win_square = Square(self.nrow - 1, self.dan_chess.column)

    x_distance = dan_win_square.column - self.sushant_chess.column
    if x_distance < 0:
      x_distance = -x_distance
    y_distance = dan_win_square.row - self.sushant_chess.row
    if y_distance < 0:
      y_distance = -y_distance

    #case 1: Y > X and reach same square
    num_2 = 0
    num_1 = 0
    if y_distance > x_distance:
      if y_distance % 2 == 0:
        num_2 = y_distance // 2
        if num_2 * 1 <= x_distance:
          return "Dan wins in {} moves".format(number_dan_win_moves-1)
        elif self.dan_chess.column != self.sushant_chess.column:
          if num_2 % 2 == 0:
            return "Dan wins in {} moves".format(number_dan_win_moves-1)
          
      else:
        num_2 = self.get_number_2(x_distance, y_distance)
        num_1 = self.get_number_1(x_distance, y_distance)
        if num_2 + num_1 != number_dan_win_moves:
          return "Dan wins in {} moves".format(number_dan_win_moves-1)
    else:
      if x_distance % 2 == 0:
        num_2 = x_distance // 2
        if num_2 * 1 <= y_distance:
          return "Dan wins in {} moves".format(number_dan_win_moves-1)
        elif self.dan_chess.row != self.sushant_chess.row:
          if num_2 % 2 == 0:
            return "Dan wins in {} moves".format(number_dan_win_moves-1)
      else:
        num_2 = self.get_number_2(y_distance, x_distance)
        num_1 = self.get_number_1(y_distance, x_distance)
        if num_2 + num_1 > number_dan_win_moves:
          return "Dan wins in {} moves".format(number_dan_win_moves-1)
    return 'sushant'
          
        
        
      
    
  def play_Game(self):
    l = [self.sushant_chess]
    
    while (True):
      # dan moves first
      if self.dan_chess.row + 1 <= self.nrow-1:
        self.dan_chess.row +=1

        self.num_dan_moves += 1
        if self.dan_chess.row == self.nrow -1:
          #return self.num_sushant_moves
          return "Dan wins in {} moves".format(self.num_sushant_moves)
          break
        
      sub_l = []
      current_l = []
      for square in l:
        sub_l = self.sushant_next_moves(square)
        square.sub_ways = sub_l
        current_l += sub_l
 
      if len(current_l) > 0:
        self.num_sushant_moves += 1

      for s in current_l:
        if (s.row == self.dan_chess.row) and (s.column == self.dan_chess.column):
          
          #return self.num_sushant_moves
          return "Sushant wins in {} moves".format(self.num_sushant_moves) 
          break
        
      l = current_l
        

        
       

def game_outcome(nrows, ncols, dan_row, dan_col, sushant_row, sushant_col):
  '''Return the appropriate string, as described in the handout.
  
  nrows: number of rows in the board
  ncols: number of columns in the board
  dan_row/dan_col: Dan's starting location
  sushant_row/sushant_col: Sushant's starting location
  '''
  dan_chess = Square(dan_row, dan_col)
  sushant_chess = Square(sushant_row, sushant_col)
  game = Game(dan_chess, sushant_chess, nrows, ncols)

  return game.play_Game()

  
  

if __name__ == '__main__':

  # some small test cases
  # Case 1, Sushant wins in 1 moves
  s = game_outcome(50, 50, 10, 10, 10, 12)
  assert s == 'Sushant wins in 1 moves'
  # Case 2, Dan wins in 2 moves
  s = game_outcome(6, 8, 2, 3, 0, 0)
  assert s == 'Dan wins in 2 moves'
