# Úkol: Útulek pro zvířata

# Funkce pro vytvoření útulku (prázdného slovníku)
def vytvor_utulek():
    return {}

# Funkce pro přidání zvířete do útulku
def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {
        "druh": druh,
        "vek": vek
    }

# Funkce pro výpis všech zvířat
def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        print(f"{jmeno} je {info['druh']} a je jí/mu {info['vek']} let.")

# (Volitelné pro pokročilé) Výpis podle druhu
def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            print(f"{jmeno} je {info['druh']} a je mu {info['vek']} let.")

# Použití funkcí (test)
utulek = vytvor_utulek()
pridej_zvire(utulek, "Míca", "kočka", 3)
pridej_zvire(utulek, "Rex", "pes", 5)

print("Všechna zvířata v útulku:")
vypis_zvirata(utulek)

print("Jen psi v útulku:")
vypis_podle_druhu(utulek, "pes")
