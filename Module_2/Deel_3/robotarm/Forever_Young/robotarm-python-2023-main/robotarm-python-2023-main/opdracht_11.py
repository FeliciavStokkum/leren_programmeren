from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

for c in range(8): #De arm gaat eerst 8 naar rechts 
    robotArm.moveRight()

for a in range(9): #De arm pakt het blokje
    robotArm.grab()
    color = robotArm.scan() #Hier scant de robotarm de kleur
    if color == "white": #Als de kleur wit is print die wit
        print("Wit")
        robotArm.moveRight() #De robotarm gaat naar rechts 
        robotArm.drop() #De robotarm dropt het blokje
        robotArm.moveLeft() #De robotarm gaat naar links
    else:
        robotArm.drop() #Als de kleur niet wit is dropt die het blokje
    if a != 8: #Als 8 niet gelijk is aan 8, gaat de robotarm nog naar links
        robotArm.moveLeft()

robotArm.wait()