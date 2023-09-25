# Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’

# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. 
# Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. 
# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

# Maak een programma speelhal.py voor deze berekening.

vr_minuten = 45 / 5

TOEGANGSTICKET = 7.45 * 4
VR_PER_PERSOON = 0.37 * vr_minuten * 4

totaal = int(TOEGANGSTICKET + VR_PER_PERSOON)

print(f"Je moet totaal {totaal} betalen.")