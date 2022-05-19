from random import randrange

N_TURN = 0


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|  ",row[0] , "  |  ", row[1] , "  |  ", row[2] , "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def is_valid(board, choice):
    # The function accepts the board's current status and check if the choice is valid
    
    try:
        choice = int(choice)
        
    except ValueError:
        print("The value is not an integer number")
        return False
    
    else:
    
        if choice < 0 or choice > 10:
            print("The value is too small or too big")
            return False
        
    free_fields = make_list_of_free_fields(board)
    all_fields = make_list_of_all_fields(board)
    
    if all_fields[choice - 1] not in free_fields:
        print("The cell is already occupied")
        return False
    
    return True


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    return [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell != 'X' and cell != 'O']


def make_list_of_all_fields(board):
    # The function browses the board and builds a list of all the squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    return [(x, y) for x in range(len(board)) for y in range(len(board))]


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # invert board
    t_board = [[board[y][x] for x in range(len(board)) for y in range(len(board[x])) if x == i] for i in range(len(board))]

    return search_linear_horizontal_win(board, sign) or search_linear_horizontal_win(t_board, sign) or search_diagonal_win(board, sign)


def search_linear_horizontal_win(board, sign):
    # the function analyzes the board's status in order to check if 
    # there is linear horizontal pattern in the board with sign
    
    is_win = False
    
    for row in board:
        if row[0] == sign and row[1] == sign and row[2] == sign :
            is_win = True
            break
            
    return is_win


def search_diagonal_win(board, sign):
    # the function analyzes the board's status in order to check if 
    # there is diagonal pattern in the board with sign
    
    return len([board[x][x] for x in range(len(board)) if board[x][x] == sign]) == len(board) or len([board[x][len(board) -1 - x] for x in range(len(board)) if board[x][len(board) - 1 - x] == sign]) == len(board)
        
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    while True:
        choice = randrange(1, 10)
        print("PC Choice: ", choice)
        if is_valid(board, choice):
            update_board(board, choice, 'X')
            break
        
def draw_first_move(board):
    # The function draws the computer's firstmove and updates the board.
    
    START_POSITION = 5
    print("PC Choice: ", START_POSITION)
    update_board(board, START_POSITION, 'X')
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        choice = input("Choose a cell[1 - 9]: ")
        print("PLAYER Choice: ", choice)
        if is_valid(board, choice):
            update_board(board, choice, 'O')
            break
    

def update_board(board, choice, sign):
    # The function updates the board.
    
    cell = make_list_of_all_fields(board)[int(choice) - 1]
    board[cell[0]][cell[1]] = sign


def create_board():
    # The function create the starting board
    
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def play():
    # The function manage the game
    
    board = create_board()
    N_TURN = 0
    print("NEW GAME")
    print("PLAYER (plays 'O')  - VS -  PC (plays 'X')")
    while True:
        
        N_TURN += 1
        print("TURN :", N_TURN)
        
        # PC plays first
        draw_first_move(board) if N_TURN == 1 else draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print('PC WINS')
            break
            
        # PLAYER plays second
        enter_move(board)
        display_board(board)
        
        if victory_for(board, 'O'):
            print('PLAYER WINS')
            break
            
        
play()

#for i in range(100):
#    print(randrange(1, 10))
# b = [[1,2,'X'], [4, 'X', 'O'], [7, 8, 9]]
# display_board(b)
# l = make_list_of_free_fields(b)
# print(l)
# print((0, 2) in l)
# l2 = [(x, y) for x in range(3) for y in range(3)]
# print(l2)

# print(l2[8] in l)

# display_board([[0,0,0], [0, 0, 0], [0, 0, 0]])
