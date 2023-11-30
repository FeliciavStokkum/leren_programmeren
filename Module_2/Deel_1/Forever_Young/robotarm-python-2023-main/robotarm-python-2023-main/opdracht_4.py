from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
for stapel in range(4):
    robotArm.grab()

    for rechts in range(2):
        robotArm.moveRight()

    robotArm.drop()

    for links in range(2):
        robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for stapel in range(4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.wait()