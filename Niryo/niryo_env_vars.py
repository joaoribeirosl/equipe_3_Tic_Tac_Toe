from pyniryo2 import *
# from niryo_initialize import robot
import random

robot = NiryoRobot("169.254.200.200")
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
Vai_pegar = robot.arm.move_joints([-1.569, -0.465, -0.716,-0.147, -0.058, -0.038]) #Posição pra pegar

#A
A1 = robot.arm.move_joints([ 0.150, -0.953, 0.224,-0.147, -0.762, -0.028])
A2 = robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033])
A3 = robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038])

#B
B1 = robot.arm.move_joints([ 0.173, -0.775, -0.155, -0.101, -0.598, 0.131])
B2 = robot.arm.move_joints([ -0.018, -0.788, -0.148, -0.147, -0.592, -0.120])
B3 = robot.arm.move_joints([ -0.177, -0.784, -0.145, -0.147, -0.592, -0.130])

#C
C1 = robot.arm.move_joints([ 0.188, -0.567, -0.521, -0.034, -0.413,  0.049])
C2 = robot.arm.move_joints([-0.031, -0.579, -0.497, -0.008, -0.503, -0.268])
C3 = robot.arm.move_joints([-0.264, -0.572, -0.449, -0.008, -0.511, -0.426])


def movendo_para_posição(positions_number):
    positions_dict = {
        1: A1,
        2: A2,
        3: A3,
        4: B1,
        5: B2,
        6: B3,
        7: C1,
        8: C2,
        9: C3,
    }

    if positions_number in positions_dict:
        robot.arm.move_joints(positions_dict[positions_number])
        print(f"Robô movido para a posição {positions_number}.")
    else:
        print("Número de célula inválido. Use um número de 1 a 9.")


    random_move = random.choice(list(positions_dict.keys()))
    target_position = positions_dict[random_move]


robot.end()
# jogada = random(1,9)
# del jogada