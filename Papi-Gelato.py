hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

Aardbei = ["Aardbei", "aardbei", "A", "a"]
Chocolade = ["Chocolade", "chocolade", "C", "c"]
Munt = ["Munt", "munt", "M", "m"]
Vanille = ["Vanille", "vanille", "V", "v"]

geen = ["geen", "Geen", "A", "a"]
slagroom = ["slagroom", "Slagroom", "B", "b"]
sprinkels = ["sprinkels", "Sprinkels", "C", "c"]
caramel = ["caramel", "Caramel", "D", "d"]

Slagroom = 0
Sprinkels = 0
Caramel = 0


VraagSmaak = True
Hoorntje = 0
Bakje = 0
AantalBolletjes = 0

Begin = True

def Topping():
    global Slagroom
    global Sprinkels
    global Caramel
    while True:
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?:")
        if topping in slagroom:
            Slagroom += 1
            break
        elif topping in sprinkels:
            Sprinkels += 1
            break
        elif topping in caramel:
            Caramel += 1
            break
        elif topping in geen:
            break
        else:
            print("Sorry dat snap ik niet...")

def smaak():
    for smaak in range(bolletjes):
            VraagSmaak = True
            while VraagSmaak:
                SmaakPerBol = input("Welke smaak wilt u voor bolletje " + str(smaak + 1) + "?  A) Aardbei, C) Chocolade, M) Munt of V) Vanille?:")
                if SmaakPerBol in Aardbei or SmaakPerBol in Chocolade or SmaakPerBol in Munt or SmaakPerBol in Vanille:
                    VraagSmaak = False
                else:
                    print("Sorry dat snap ik niet...")
                    VraagSmaak = True

while Begin:
    print("Welkom bij Papi Gelato.")
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    AantalBolletjes += bolletjes
    if bolletjes <= 3:        
        smaak()
        HoorntjeBakje = (input("Wilt u deze " + str(bolletjes) + " in een hoorntje of een bakje? :"))
        if HoorntjeBakje in hoorntjeLijst or HoorntjeBakje in bakjeLijst:
            Begin = False
            if HoorntjeBakje in hoorntjeLijst:
                Hoorntje += 1
                Topping()
            elif HoorntjeBakje in bakjeLijst:
                Bakje += 1
                Topping()
            Meer = input("Hier is uw " + str(HoorntjeBakje) + " met " + str(bolletjes) + " bolletjes. Wilt u nog meer bestellen? Y/N :")
            if Meer in Yes:
                Begin = True
            elif Meer in No:
                Begin = False
                print("Bedankt en tot ziens!")
            else:   
                print("Sorry dat snap ik niet...")
    elif bolletjes >= 4 and bolletjes <=8:
        smaak()
        Topping()
        Bakje += 1
        HoorntjeBakje = bakjeLijst
        print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes.")
        Begin = False
    elif bolletjes >8:        
        print("Sorry zulke grote bakken hebben wij niet")
        Begin = True
    else:
        print("Sorry dat snap ik niet...")

SlagroomPrijs = Slagroom*0.50
SprinkelsPrijs = Sprinkels*0.30*bolletjes
if HoorntjeBakje in hoorntjeLijst:
    CaramelPrijs = Caramel*0.60
elif HoorntjeBakje in bakjeLijst:
    CaramelPrijs = Caramel*0.90
CaramelPrijs = 0

ToppingPrijs = SlagroomPrijs + SprinkelsPrijs + CaramelPrijs


Bolletjes = AantalBolletjes*1.10
Hoorntjes = Hoorntje*1.25
Bakjes = Bakje*0.75
Totaal = Bolletjes + Hoorntjes + Bakjes + ToppingPrijs

print("----------[Papi Gelato]----------")
print(f"Bolletjes    {bolletjes} X €1.10  = €{Bolletjes:.2f}")
if HoorntjeBakje in hoorntjeLijst:
    print(f"Hoorntje     {Hoorntje} X €1,25  = €{Hoorntjes:.2f}")
else:
    print(f"Bakje         {Bakje} X €0.75 = €{Bakjes:.2f}")

if Slagroom > 0 or Sprinkels > 0 or Sprinkels > 0 or Caramel > 0:
    print(f"Topping        1 X €{ToppingPrijs:.2f} = €{ToppingPrijs:.2f}")

print("                         -------- +")
print(f"                        = €{Totaal:.2f}")