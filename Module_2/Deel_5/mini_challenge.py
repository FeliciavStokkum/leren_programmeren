cijferlijst = [10, 9, 7, 2, 15, 16, 13, 11, 9]

cijferlijst_2 = []
for cijfer in cijferlijst:
    if cijfer in range(1, 11):
        cijferlijst_2.append(cijfer)
print(cijferlijst_2)

for cijfer in cijferlijst[::]:
    if cijfer > 10:
        cijferlijst.remove(cijfer)
print(cijferlijst)

#Dit wordt het meest gebruikt
print(list(filter(lambda a: a < 11, cijferlijst)))