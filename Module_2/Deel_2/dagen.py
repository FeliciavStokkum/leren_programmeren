dagen_van_de_week = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag") 

print("\nDit zijn alle dagen van de week:")
for dag in dagen_van_de_week:
    print(dag)

print("\nDit zijn de werkdagen:")
for werkdagen in dagen_van_de_week[:5]:
    print(werkdagen)

print("\nDit zijn de dagen in omgekeerde volgorde:")
for omgekeerde_dagen in dagen_van_de_week[::-1]:
    print(omgekeerde_dagen)

print("\nDit zijn de werkdagen omgekeerd:")
for omgekeerde_werkdagen in dagen_van_de_week[4::-1]:
    print(omgekeerde_werkdagen)

print("\nDit zijn de weekenddagen omgekeerd:")
for omgekeerde_weekenddagen in dagen_van_de_week[-1:4:-1]:
    print(omgekeerde_weekenddagen)