from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

stappen = 1

while True:
    robotArm.grab()
    blok = robotArm.scan()
    if blok == "":
        break
    else:
        stappen += 1
        for x in range(stappen):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(stappen):
            robotArm.moveLeft()
        
robotArm.wait()