from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
for a in range(7):
    robotArm.moveRight()
    robotArm.grab()
    for i in range(8):  
        robotArm.moveRight()
    robotArm.drop()
    for b in range(9):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 