from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

while True:
    robotArm.grab()
    robotArm.scan()
    color = robotArm.scan()
    if color == "red":
        for x in range():
            robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()

robotArm.wait()