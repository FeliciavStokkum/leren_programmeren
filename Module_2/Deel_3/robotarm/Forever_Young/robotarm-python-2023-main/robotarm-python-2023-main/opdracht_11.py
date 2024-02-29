from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

stappen_links = 8

for c in range(8):
    robotArm.moveRight()

while True:
    robotArm.grab()
    robotArm.scan()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()

    if stappen_links > 0:
        robotArm.moveLeft()
        stappen_links -= 1
    elif stappen_links == 0:
        break

robotArm.wait()
