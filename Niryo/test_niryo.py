from pyniryo2 import *
from niryo_initialize import robot
robot = NiryoRobot("169.254.200.200")

robot.arm.calibrate_auto()
robot.tool.update_tool() 
robot.tool.release_with_tool()



posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
Vai_pegar = robot.arm.move_joints([-1.577, -0.493, -0.692,-0.147, -0.074, -0.028]) #Posição pra pegar
robot.tool.grasp_with_tool() 
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
A1 = robot.arm.move_joints([ 0.150, -0.953, 0.224,-0.147, -0.762, -0.028]) #A1
robot.tool.release_with_tool() 
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
Vai_pegar = robot.arm.move_joints([-1.577, -0.493, -0.692,-0.147, -0.074, -0.028]) #Posição pra pegar
robot.tool.grasp_with_tool() 
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
A2 = robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033]) #A2
robot.tool.release_with_tool() 
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
Vai_pegar = robot.arm.move_joints([-1.577, -0.493, -0.692,-0.147, -0.074, -0.028]) #Posição pra pegar
robot.tool.grasp_with_tool() 
posicao_para_andar = robot.arm.move_joints([-1.577, -0.178, -0.693,-0.018, -0.500, -0.084]) #Posição anterior e posterior de pegar
A3 = robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038]) #A3
robot.tool.release_with_tool() 

# A2 = robot.arm.move_joints([ 0.000, -0.952, 0.206, -0.147, -0.762, -0.033]) #A2
# A3 = robot.arm.move_joints([ -0.157, -0.980, 0.248, -0.147, -0.762, -0.038]) #A3

# #B
# B1 = robot.arm.move_joints([ 0.173, -0.775, -0.155, -0.101, -0.598, 0.131]) #B1
# B2 = robot.arm.move_joints([ -0.018, -0.788, -0.148, -0.147, -0.592, -0.120]) #B2
# B3 = robot.arm.move_joints([ -0.177, -0.784, -0.145, -0.147, -0.592, -0.130]) #B3


# #C
# C1 = robot.arm.move_joints([ 0.188, -0.567, -0.521, -0.034, -0.413,  0.049]) #C1
# C2 = robot.arm.move_joints([-0.031, -0.579, -0.497, -0.008, -0.503, -0.268]) #C2
# C3 = robot.arm.move_joints([-0.264, -0.572, -0.449, -0.008, -0.511, -0.426]) #C3



# robot.tool.update_tool() 
# robot.tool.release_with_tool() 
# robot.tool.grasp_with_tool() 
# # robot.arm.set_arm_max_velocity(x)
# robot.saved_poses.get_pose_saved()

robot.end()
