from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')

# Jouw python instructies zet je vanaf hier:
# Na jouw code wachten tot het sluiten van de window:
# robotArm.wait()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.wait()