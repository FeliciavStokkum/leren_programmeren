from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

stappen = 1

while True:
    robotArm.grab()
    blok = robotArm.scan()
    if blok == "blue" or blok == "":
        if blok == "blue":
            robotArm.drop()
        break
    else:
        for x in range(stappen):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(stappen):
            robotArm.moveLeft()
        stappen += 1
        
robotArm.wait()
