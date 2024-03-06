from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')

# aantal = 5
# for x in range(1, 11):
#     robotArm.grab()
#     for i in range(5):
#         robotArm.moveRight()
#     robotArm.drop()
#     if x == 1 or x == 3 or x == 6:
#         aantal = 4
#     else:
#         aantal = 5
#     for i in range(aantal): robotArm.moveLeft()

for stapel in range(1,5):
    for blokje in range(stapel):
        robotArm.grab()
        for move in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for move in range(5):
            robotArm.moveLeft()     
    robotArm.moveRight()  


robotArm.wait()