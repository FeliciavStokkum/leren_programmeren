from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

# stappen_links = 8
# stappen_rechts = 1

for c in range(8):
    robotArm.moveRight()

for positie in range(8, -1, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        print("Red")
        for move in range(9 - positie):
            robotArm.moveRight()
        robotArm.drop()
        for move_2 in range(9 - positie):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    if positie != 0:
        robotArm.moveLeft()

# while True:
#     robotArm.grab()
#     robotArm.scan()
#     color = robotArm.scan()
#     if color == "red":
#         for x in range(stappen_rechts):
#             robotArm.moveRight()
#         robotArm.drop()
#         for x in range(stappen_rechts):
#             robotArm.moveLeft()
#     else:
#         robotArm.drop()

#     if stappen_links > 0:
#         robotArm.moveLeft()
#         stappen_rechts += 1
#         stappen_links -= 1
#     elif stappen_links == 0:
#         break

robotArm.wait()