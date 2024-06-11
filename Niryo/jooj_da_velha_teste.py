import random
from pyniryo2 import *
from niryo_initialize import robot


# print('robô calibrado!')

# print('robô se prepara pra pegar uma peça...')

robot.arm.calibrate_auto()
robot.tool.update_tool() 
robot.tool.release_with_tool()

posicao_para_andar = robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar

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

positions = {
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
      
    while playing:
        draw_board(board)
        try:
            if current_player == 'O':
                # print('o robô segura a peça e fecha a garra')
                robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #alto
                robot.arm.move_joints([-1.597, -0.489, -0.678,-0.009, -0.144, -0.150]) #baixo
                robot.tool.grasp_with_tool()
                move = random.choice(list(positions_dict.keys())) 
                robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar     
                print(f'Vez do robô e ele vai jogar na posição {move}...')
                urgent_move(move) 
                print(f'o robô joga na posição {move}!')
                robot.tool.release_with_tool() 
                robot.arm.move_joints([-1.603, -0.156, -0.834,-0.012, -0.157, -0.140]) #Posição anterior e posterior de pegar  
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

def urgent_move(move):
    if move == 1: robot.arm.move_joints([ 0.150, -0.953, 0.224,-0.147, -0.762, -0.028])
    if move == 2: robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033])
    if move == 3: robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038])
    if move == 4: robot.arm.move_joints([ 0.173, -0.775, -0.155, -0.101, -0.598, 0.131])
    if move == 5: robot.arm.move_joints([ -0.018, -0.788, -0.148, -0.147, -0.592, -0.120])
    if move == 6: robot.arm.move_joints([ -0.177, -0.784, -0.145, -0.147, -0.592, -0.130])
    if move == 7: robot.arm.move_joints([ 0.188, -0.567, -0.521, -0.034, -0.413,  0.049])
    if move == 8: robot.arm.move_joints([-0.031, -0.579, -0.497, -0.008, -0.503, -0.268])
    if move == 9: robot.arm.move_joints([-0.264, -0.572, -0.449, -0.008, -0.511, -0.426])




if __name__ == "__main__":
    game_loop()
    print('robô desligado')