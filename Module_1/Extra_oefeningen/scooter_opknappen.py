BAND = 57,79
ARBEID_PER_BAND = 15,00
NIEUWE_LAMP = 1,45
LAMPJES_VERVANGEN_PS = 2,10

kosten_nieuwe_banden = 2 * BAND 
kosten_arbeid_banden = 2 * ARBEID_PER_BAND

kosten_nieuwe_lamp = 2 * NIEUWE_LAMP 
kosten_arbeid_lampen = 2 * LAMPJES_VERVANGEN_PS

Totaalkosten = (kosten_nieuwe_banden + kosten_arbeid_banden) + (kosten_nieuwe_lamp + kosten_arbeid_lampen)
Totaalkosten = 115,58 + 30,00 + 2,90 + 4,20

print(f"Uw totaal kosten zijn: {Totaalkosten}")
