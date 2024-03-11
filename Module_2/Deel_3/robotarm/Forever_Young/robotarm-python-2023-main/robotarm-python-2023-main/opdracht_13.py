from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

stappen = 1

while True: #Zolang dit waar is, speelt hij dit af. Aangezien het level telkens een andere hoeveelheid blokjes heeft is dit het makkelijkst om te doen. 
    robotArm.grab() #Hier pakt de robotarm een blokje
    blok = robotArm.scan() #Hier scant de robotarm het blokje
    if blok == "blue" or blok == "": #Als het blokje blauw is of als er geen blokje meer is
        if blok == "blue":
            robotArm.drop() #als het blokje blauw is dropt hij het blokje
        break  #dan stopt die de while lus
    else:
        for x in range(stappen):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(stappen):
            robotArm.moveLeft()
        stappen += 1 #Anders zet die stappen heen en dezelfde aantal stappen terug
        
robotArm.wait()