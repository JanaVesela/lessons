
# výpis prvnich 5 znaku
print("indexovani"[:5])

#výpis posledních pšti znaků
print("indexovani"[-5:])

#výpis každého třetího písmene (počínaje prvním) od 'i'
print("indexování"[::3])

kg_lb = 2.20
km_mile= 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet

print(kg_pocet,'kg je' , kg, kg_vysledek, 'lb')
print(km_pocet, 'km je', km, km_vysledek, 'mile')
print(l_pocet, 'l je', 'l', l_vysledek, 'gal')

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000

cena_2_merc = mercedes * 2
print(mercedes * 2)

cena_merc_a_rolls = mercedes + rolls_royce
print(mercedes + rolls_royce)

cena_2_rolls_s_vybavou = 2 * rolls_royce + 2 * vybava
print((2*rolls_royce)+(2*vybava))

cena_merc_s_vybavou = mercedes + vybava
print(mercedes+vybava)

merc_se_slevou = mercedes - sleva_merc
print(mercedes-sleva_merc)

print ("sleva na mercedes:", sleva_merc)
print ("cena za dva mercedesy je:", cena_2_merc)
print ("cena za mercedes a rolls-royce je:", cena_merc_a_rolls)
print ("cena za dva rolls-royce s priplatkovou vybavou je:", cena_2_rolls_s_vybavou)
print ("cena za mercedes s priplatkovou výbavou je:", cena_merc_s_vybavou)
print ("cena za mercedes po slevě je:", merc_se_slevou)

jmeno = "Lukas"
prijmeni = "Dvořák"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)



print("celé jmeno", cele_jmeno)
print("délka jména", delka_jmena)


print("="*delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)