def draw_board():
    print (('_' * 4 * 3 ))
    for i in range(3):
     print ((' ' * 3 + '|') * 3)
     print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
     print (('_' * 3 + '|') * 3)

def check_win():
    win = False
    win_combination = (
     (0,1,2), (3,4,5), (6,7,8),
     (0,3,6), (1,4,7), (2,5,8),
     (0,4,8), (2,4,6)
     )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','0')):
            win = board[pos[0]] 

    return win

def game_step(index, char):
    if (index > 9 or index < 1 or (board[index-1] in ('X','0'))):
        return False

    board[index-1] = char
    return True

def start_game():
    global score1, score2
    draw_board()
    player = "X"
    step = 0
    while check_win() == False and step != 9:
        index = input('go ' + player + '. Enter the field number:')

        if (game_step(int(index), player) == True):
            draw_board()
            if (player == 'X'):
                player = '0'
            else:
                player = 'X'
            step += 1
        else:
            print("Invalid number")
            continue
    if check_win() == current_player.upper():
        score1 += 1
    elif check_win() == next_player.upper():
        score2 += 1

    if str(check_win()) in "X0":
        print('Won ' + check_win())
    else:
        print("Draw")
    print(f"{player1} has {score1} scores and {player2} has {score2} scores ")


player1 = input("First player: ")
player2 = input("Second player: ")
rounds = input("Rounds number: ")
score1 = 0
score2 = 0
for i in range(int(rounds)):
    board = [1,2,3,4,5,6,7,8,9]
    print(f"{i+1} round")
    current_player = input(f"{player1}'s symbol: (x/0)")
    if (current_player == 'X'):
        next_player = '0'
    else:
        next_player = 'X'

    start_game()
if score1 > score2:
    print(f"{player1} win!")
elif score1 < score2:
    print(f"{player2} win!")
else:
    print("Draw.")

#case_win = "x" = symbol_1 = p_1 = p_1 = win = socre_1 +=1
Zhansara
Altynay
