from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
for stapel in range(5):
    robotArm.moveRight()
    for blokje in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if stapel < 4:
        robotArm.moveRight() # naar de volgende stapel
robotArm.wait()