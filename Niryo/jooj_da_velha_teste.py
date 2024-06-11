# from niryo_env_vars import *
import random

print('robô calibrado!')

print('robô se prepara pra pegar uma peça...')

def draw_board_with_numbers():
    print(' 7 | 8 | 9 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 1 | 2 | 3 ')
    
def edit_board(board, row, col, current_player):
    board[row][col] = current_player    
      
      
def draw_board(board):
    for i in range(3):
        print(' ' + ' | '.join(board[i]))
        if i < 2:
            print('---+---+---')

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def game_loop():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    playing = True
    current_player = 'X'

    print('\n\n\n𝓫𝓮𝓶 𝓿𝓲𝓷𝓭𝓸 𝓪𝓸 𝓳𝓸𝓰𝓸 𝓭𝓪 𝓿𝓮𝓵𝓱𝓪, 𝓶𝓮𝓾𝓼 𝓫𝓪𝓬𝓪𝓷𝓸𝓼!')
    player_1 = input('\ninforme o nome do jogador 1: (vai começar jogando) ')
    player_2 = 'Robô Niryo' 

    players = { 'X': player_1, 'O': player_2 }

    print('o negócio é o seguinte meu parceiro, tu vai digitar o número do lugar que você quer jogar.')
    print('Na dúvida, olhe o seu teclado numérico. Observe o tabuleiro abaixo: \n\n')

    draw_board_with_numbers()
    print('\n')

    positions = {
        7: (0, 0), 8: (0, 1), 9: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        1: (2, 0), 2: (2, 1), 3: (2, 2)
    }
    

    positions_dict = {
        1: 'pos1',
        2: 'pos2',
        3: 'pos3',

        4: 'pos4',
        5: 'pos5',
        6: 'pos6',

        7: 'pos7',
        8: 'pos8',
        9: 'pos9'
    }
    
      
    while playing:
        draw_board(board)
        try:
            if current_player == 'O':
                print('o robô segura a peça e fecha a garra')
                move = random.choice(list(positions_dict.keys())) 
                print(f'Vez do robô e ele vai jogar na posição {move}...')
                positions_dict[move]
                # urgent_move(move) 
                print(f'o robô joga na posição {move}!')
                if move in positions_dict:
                    del positions_dict[move] 
                row, col = positions[move]
                if board[row][col] != ' ':
                    print('Essa posição já está ocupada. Escolha outra.\n')
            if current_player == 'X':
                move = int(input(f'\n{players[current_player]}, escolha onde você vai jogar (1-9): \n\n'))
                if move in positions_dict:
                    del positions_dict[move]
                if move not in positions:
                    raise ValueError
                row, col = positions[move]
                if board[row][col] != ' ':
                    print('Essa posição já está ocupada. Escolha outra.\n')
                
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número entre 1 e 9.\n')
    
        board[row][col] = current_player

        if check_winner(board, current_player):
            draw_board(board)
            print(f'\nPARABAINXXX, {players[current_player]}! AO VENCEDOR AS BATATAS!\n')
            playing = False
        elif all(all(cell != ' ' for cell in row) for row in board):
            draw_board(board)
            print('\ndeu velha pessoal kkkkkjjj!\n')
            playing = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

    if input('\nQuer jogar novamente? (s/n): ').lower() == 's':
        game_loop()


if __name__ == "__main__":
    game_loop()
    print('robô desligado')
