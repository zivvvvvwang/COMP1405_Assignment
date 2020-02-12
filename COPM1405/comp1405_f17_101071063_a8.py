# ============================================================
#
# Student Name (as it appears on cuLearn): Ziwen Wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================


'''
This is an introduction function, to give user introduction
@ params      none

@ return      none
'''
def introduction():
    print("This is an introduction of this program:\n* In this program, the \"-\" respresent empty space\n\t\t   the \"K/k\" represent King\n\t\t   the \"Q/q\" represent Queen\n\t\t   the \"B/b\" represent Bishop\n\t\t   the \"N/n\" represent Knight\n\t\t   the \"R/r\" represent Rook\n\t\t   the \"P/p\" represent Pawn\n* The lowercase represent white piece and uppercase represent black piece\n* You will be ask to enter the state chessboard(8*8) use above letters, which means you will be ask 8 times for 8 letters enter. \n* You can select move or quit when you initialized the chessboard, you will be asked two coordinates to get the point that you want to move, and you will be asked other two coordinates to get the point that you would like to move to..\n")
    return

'''
This function will print an initiallize chessboard
@ params      none

@ return      move    the board of current 
'''
def initialize_chessboard():
    size = 8
    whole = []
    letter = ["  "]
    score = []
    move = []
    for x in range(65,73):
        letter.append(chr(x))
    whole.append(letter)
    for i in range(size):
        row = []
        user_input = "Please enter the " + str(i + 1) +" row: "
        row.append(str(i+1) + " ")
        check_result = error_check(user_input)
        row.append(check_result)
        whole.append(row)
        score.append(check_result)
        move.append(row)
    for t in whole:
        for w in t:
            print(w,end = "")
        print()
    print("The score of white piece is " + str(white_score(score)))
    print("The score of black piece is " + str(black_score(score)))
    return move

'''
This is select option function, to give user a select menu
@ params      none

@ return      flag    user want to move or quit
'''
def select_option():
    flag = True
    selection = int(input("Please make a selection: \n1. Move \n2. Quit\n"))
    if selection == 1:
        return flag
    else:
        flag = False
        return flag
    
'''
This function in order to move chess in board
@ params      board    The current board state

@ return      none
'''
def piece_move(board):
    whole = []
    number = 8
    count = 0
    row_list = ["  "]
    score = []
    letter = ""
    moveletter = ""
    piece = ["k","q","b","r","p","n","K","Q","B","R","P","N"]
    for x in range(65,73):
        row_list.append(chr(x))
    whole.append(row_list)
    while True:
        
        row = int(input("\nPlease enter the row number that the piece stands(1-8): "))
        col = input("Please enter the col number that the piece stands(A-H): ").upper()
        col_number = ord(col)
        if row < 1 or row > 8 or col_number <65 or col_number > 72:
            print("Error, out of range, please enter again! ")
        else:
            break
    for i in board[row-1][1]:
        if col_number - 65 == board[row-1][1].index(i):
            letter = i
                    
            if letter not in piece:
                print("There is no piece here, please enter again! ")
                    
            else:
                moverow = int(input("\nPlease enter the row number that the piece going to (1-8): "))
                movecol = input("Please enter the col number that the piece going to (A-H): ").upper()
                if moverow < 1 or moverow > 8 or ord(col) <65 or ord(col) > 72:
                    print("Error, out of range, please enter again! ")
            
                        
    for j in board[moverow-1][1]:
        if ord(col) - 65 == board[moverow-1][1].index(j):
            moveletter = j
            board[moverow-1][1]== letter
            board[row-1][1]== "-"
        if letter not in piece:
            print("There is no piece here, please enter again! ")
                                     
    for t in board[1:1]:
        for f in t:
            score.append(f)
           
    whole.append(board)
    for a in whole[0]:
        print(a,end = "")
    print()
    for b in whole[1]:
        for c in b:
            print(c,end = "")
        print()
        
       
    print("\nThe score of white piece is " + str(white_score(score)))
    print("The score of black piece is " + str(black_score(score)))
    return

'''
This is an error check function
@ params      arg

@ return      user_input
'''
def error_check(arg):
    while True:
        user_input = input(arg)
        count = 0
        if len(user_input) != 8:
            print("Sorry! you need to enter 8 element each raw! ")
        else:
            for i in user_input:
                if i == "-":
                    count += 0
                elif i == "k" or i == "K":
                    count += 0
                elif i == "q" or i == "Q":
                    count += 0
                elif i == "b" or i == "B":
                    count += 0
                elif i == "r" or i == "R":
                    count += 0
                elif i == "p" or i == "P":
                    count += 0
                elif i == "n" or i == "N":
                    count += 0
                else:
                    count += 1
            if count != 0:
                print("Sorry! you need to use \"-\",\"K\k\",\"Q/q\",\"B/b\",\"R/r\",\"P/p\",\"n/N\" to make a chess board!")
            else:    
                break
    return user_input

'''
This is an score caculation function, to caculate white chess score
@ params      board

@ return      score
'''
def white_score(board):
    score = 0
    chess = ["-","k","q","b","r","p","n","K","Q","B","R","P","N"]
    value = [0,0,10,3,5,1,3.5,0,0,0,0,0,0]
    for j in board:
        for i in j:
            
            chess_location = chess.index(i)
            value_location = value[chess_location]
            score += value_location
    return score

'''
This is an score caculation function, to caculate black chess score
@ params      board

@ return      score
'''
def black_score(board):
    score = 0
    chess = ["-","K","Q","B","R","P","N","k","q","b","r","p","n"]
    value = [0,0,10,3,5,1,3.5,0,0,0,0,0,0]
    for j in board:
        for i in j: 
            chess_location = chess.index(i)
            value_location = value[chess_location]
            score += value_location
    return score

'''
This is an main function
@ params      none

@ return      none
'''    
def main():
    
    introduction()
    chess = initialize_chessboard()
    while True:
        if select_option() == True:
            piece_move(chess)
        else:
            break
main()
