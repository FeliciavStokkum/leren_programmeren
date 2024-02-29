# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 12')

# while True:
#     robotArm.grab()
#     robotArm.scan()
#     color = robotArm.scan()
#     if color == "red":
#             robotArm.moveRight()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()

# robotArm.wait()


from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

stappen_links = 8
stappen_rechts = 1

for c in range(8):
    robotArm.moveRight()

while True:
    robotArm.grab()
    robotArm.scan()
    color = robotArm.scan()
    if color == "red":
        for x in range(stappen_rechts):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(stappen_rechts):
            robotArm.moveLeft()
    else:
        robotArm.drop()

    if stappen_links > 0:
        robotArm.moveLeft()
        stappen_rechts += 1
        stappen_links -= 1
    elif stappen_links == 0:
        break

robotArm.wait()
