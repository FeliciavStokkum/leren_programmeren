from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

# stappen_links = 8
# stappen_rechts = 1

for c in range(8): #Eerst gaat de robotarm naar rechts
    robotArm.moveRight()

for positie in range(8, -1, -1): #hier heeft de robotarm meerdere stappen, telkens gaat hij een stapje terug en stopt bij 0
    robotArm.grab() #Robotarm pakt een blokje
    color = robotArm.scan() #Hier scant de robotarm een blokje
    if color == "red": #Als het blokje rood is, print hij "rood"
        print("Red")
        for move in range(9 - positie): #Hier berekend hij hoeveel stappen hij heen moet. Door 9 min de positie te doen. 
            robotArm.moveRight()
        robotArm.drop()
        for move_2 in range(9 - positie): #Hier bereknd hij hoeveel stappen hij terug moet. Door 9 min positie te doen. Dit is precies hetzelfde als heen.
            robotArm.moveLeft()
    else: #Als de kleur niet rood is, dropt de robotarm het blokje
        robotArm.drop()
    if positie != 0: #Als de positie niet gelijk aan 0 is gaat hij nog eentje naar links
        robotArm.moveLeft()

robotArm.wait()