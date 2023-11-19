from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
# robotArm.wait()

robotArm.grab()

for a in range(9):
    robotArm.moveRight()

robotArm.drop()

for b in range(5):
    robotArm.moveLeft()

robotArm.grab()

for c in range(5):
    robotArm.moveRight()

robotArm.drop()

for d in range(2):
    robotArm.moveLeft()

robotArm.grab()

for e in range(2):
    robotArm.moveRight()

robotArm.drop()
robotArm.wait