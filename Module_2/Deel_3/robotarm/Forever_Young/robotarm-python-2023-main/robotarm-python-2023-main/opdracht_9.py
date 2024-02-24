from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# # Jouw python instructies zet je vanaf hier:
for i in range(1):
    robotArm.grab()
    for a in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(4):
        robotArm.moveLeft()
    robotArm.grab()
    for c in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for d in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for e in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for f in range(4):
        robotArm.moveLeft()
    robotArm.grab()
    for g in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for h in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for j in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for k in range(5):
        robotArm.moveRight()
    robotArm.drop()


# # Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
