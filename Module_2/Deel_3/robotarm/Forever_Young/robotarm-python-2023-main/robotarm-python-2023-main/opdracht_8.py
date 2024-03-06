from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')

robotArm.moveRight()
# Jouw python instructies zet je vanaf hier:
for blokje in range(7):
    robotArm.grab()
    for i in range(8):  
        robotArm.moveRight()
    robotArm.drop()
    if blokje < 6:
        for b in range(8):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 