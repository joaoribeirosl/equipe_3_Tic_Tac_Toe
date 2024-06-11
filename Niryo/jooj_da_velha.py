# from niryo_env_vars import *
import random
from pyniryo2 import *
from niryo_initialize import robot

robot.arm.calibrate_auto()
robot.tool.update_tool() 
robot.tool.release_with_tool()

posicao_para_andar = robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar
# vai_pegar = robot.arm.move_joints([-1.524, -0.516, -0.668,-0.008, -0.134, -0.191]) #Posição pra pegar
# # robot.tool.grasp_with_tool()
# posicao_para_andar = robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar


def draw_board_with_numbers():
    print(' 7 | 8 | 9 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 1 | 2 | 3 ')
      
      
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

    positions_human = {
        9: (0, 0), 8: (0, 1), 7: (0, 2),
        6: (1, 0), 5: (1, 1), 4: (1, 2),
        3: (2, 0), 2: (2, 1), 1: (2, 2)
    }

    positions_dict = {
        1: robot.arm.move_joints([ 0.150, -0.953, 0.224,-0.147, -0.762, -0.028]),
        2: robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033]),
        3: robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038]),

        4: robot.arm.move_joints([ 0.173, -0.775, -0.155, -0.101, -0.598, 0.131]),
        5: robot.arm.move_joints([ -0.018, -0.788, -0.148, -0.147, -0.592, -0.120]),
        6: robot.arm.move_joints([ -0.177, -0.784, -0.145, -0.147, -0.592, -0.130]),

        7: robot.arm.move_joints([ 0.188, -0.567, -0.521, -0.034, -0.413,  0.049]),
        8: robot.arm.move_joints([-0.031, -0.579, -0.497, -0.008, -0.503, -0.268]),
        9: robot.arm.move_joints([-0.264, -0.572, -0.449, -0.008, -0.511, -0.426]),
    }
    
      
    while playing:
        draw_board(board)
        try:
            if players[current_player] == 'O':
                # robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar
                robot.arm.move_joints([-1.524, -0.516, -0.668,-0.008, -0.134, -0.191]) #Posição pra pegar
                robot.tool.grasp_with_tool()   
                move = random.choice(list(positions_dict.keys())) 
                print(f'Vez do robô e ele vai jogar na posição {move}')
                robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar     
                positions_dict[move]
                robot.tool.release_with_tool() 
                robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar  
                del positions_dict[move]
            if players[current_player] == 'X':
                move = int(input(f'\n{players[current_player]}, escolha onde você vai jogar (1-9): \n\n'))
                del positions_dict[move]
                if move not in positions_human:
                    raise ValueError
                row, col = positions_human[move]
            if board[row][col] != ' ':
                print('Essa posição já está ocupada. Escolha outra.\n')
                continue
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número entre 1 e 9.\n')
            continue

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

game_loop()
robot.end()

        ##CUIDADO, NÃO MEXER, FRÁGIL
        # if move == 1: robot.arm.move_joints([ 0.150, -0.953, 0.224,-0.147, -0.762, -0.028])
        # if move == 2: robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033])
        # if move == 3: robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038])
        # if move == 4: robot.arm.move_joints([ 0.173, -0.775, -0.155, -0.101, -0.598, 0.131])
        # if move == 5: robot.arm.move_joints([ -0.018, -0.788, -0.148, -0.147, -0.592, -0.120])
        # if move == 6: robot.arm.move_joints([ -0.177, -0.784, -0.145, -0.147, -0.592, -0.130])
        # if move == 7: robot.arm.move_joints([ 0.188, -0.567, -0.521, -0.034, -0.413,  0.049])
        # if move == 8: robot.arm.move_joints([-0.031, -0.579, -0.497, -0.008, -0.503, -0.268])
        # if move == 9: robot.arm.move_joints([-0.264, -0.572, -0.449, -0.008, -0.511, -0.426])

