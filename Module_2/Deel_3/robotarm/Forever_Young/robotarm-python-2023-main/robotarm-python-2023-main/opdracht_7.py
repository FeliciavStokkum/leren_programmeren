from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
for i in range(5):
    robotArm.moveRight()
    for b in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if i < 4:
        robotArm.moveRight()
robotArm.wait()