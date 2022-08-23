def tctctoe(board):
    n = m = 3
    
    num_x = 0
    num_o = 0
    num__ = 0
    for i in range(n):
        for j in range(m):
            num_x += int(board[i][j] == 'X')
            num_o += int(board[i][j] == 'O')
            num__ += int(board[i][j] == '_')

    if num_x - num_o > 1 or num_x < num_o: return 3
    
    player_won = False
    horizontal = False

    if board[0][0] == board[0][1] == board[0][2] != '_':
        player_won = board[0][0]
        horizontal = True

    if board[1][0] == board[1][1] == board[1][2] != '_':
        if player_won: return 3
        player_won = board[1][0]
        horizontal = True

    if board[2][0] == board[2][1] == board[2][2] != '_':
        if player_won: return 3
        player_won = board[2][0]
        horizontal = True

    if board[0][0] == board[1][0] == board[2][0] != '_':
        if player_won: return 1
        player_won = board[0][0]

    if board[0][1] == board[1][1] == board[2][1] != '_':
        if player_won: 
            if not horizontal: 
                return 3
        player_won = board[0][1]

    if board[0][2] == board[1][2] == board[2][2] != '_':
        if player_won: 
            if not horizontal: return 3
        player_won = board[0][2]
    
    if board[0][0] == board[1][1] == board[2][2] != '_' or board[2][0] == board[1][1] == board[0][2] != '_':
        player_won = board[1][1]

    
    if player_won == 'X':
        if num_x == num_o:
            return 3
    elif player_won == 'O':
        if num_x > num_o:
            return 3
    
    
    return 2 if num__ and not player_won else 1


if __name__ == '__main__':
    for _ in range(int(input())):
        board = []
        for _ in range(3):
            board.append(list(input()))
        print(tctctoe(board))