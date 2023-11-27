from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
for move_stack in range(0, 4):
    robotArm.grab()
    for right_movement in range(0, 2):
        robotArm.moveRight()
    robotArm.drop()
    for right_movement in range(0, 2):
        robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for move_stack in range(0, 4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.wait()