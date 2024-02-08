from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for a in range(7):
    robotArm.moveRight()

for b in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

    if b < 7:
        for c in range(2):
            robotArm.moveLeft()

robotArm.wait()
