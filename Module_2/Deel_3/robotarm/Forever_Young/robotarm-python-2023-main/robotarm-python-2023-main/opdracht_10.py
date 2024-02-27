from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')

bewegingen = 9

for i in range(5):
    robotArm.grab()
    for _ in range(bewegingen):  
        robotArm.moveRight()
    robotArm.drop()
    bewegingen -= 1
    for _ in range(bewegingen):
        robotArm.moveLeft()
    bewegingen -= 1

robotArm.wait()