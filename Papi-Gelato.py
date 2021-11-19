hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

Aardbei = ["Aardbei", "aardbei", "A", "a"]
Chocolade = ["Chocolade", "chocolade", "C", "c"]
# Munt = ["Munt", "munt", "M", "m"]
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

particulierLijst = ["particulier", "Particulier"]
zakelijkLijst = ["zakelijk", "Zakelijk"]

bolletjes = 0
ijsLiter = 0
HoorntjeBakje = "bakje"

Begin = True

def sorry():
    print("Sorry dat is geen optie die we aanbieden...")

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
            sorry()

def smaak():
    for smaak in range(bolletjes):
            VraagSmaak = True
            while VraagSmaak:
                SmaakPerBol = input("Welke smaak wilt u voor bolletje " + str(smaak + 1) + "?  A) Aardbei, C) Chocolade of V) Vanille?:")
                if SmaakPerBol in Aardbei or SmaakPerBol in Chocolade or SmaakPerBol in Vanille:
                    VraagSmaak = False
                else:
                    sorry()
                    VraagSmaak = True

while True:
    ParticulierZakelijk = input("Bent u particulier of zakelijk?:")
    if ParticulierZakelijk in particulierLijst:
        break
    if ParticulierZakelijk in zakelijkLijst:
        break
    else:
        sorry()

if ParticulierZakelijk in particulierLijst:
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
                    sorry()
        elif bolletjes >= 4 and bolletjes <=8:
            smaak()
            Topping()
            Bakje += 1
            HoorntjeBakje = bakjeLijst
            print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes.")
            Begin = False
        elif bolletjes >8:        
            sorry()
            Begin = True
        else:
            sorry()
elif ParticulierZakelijk in zakelijkLijst:
    ijsLiter = int(input("Hoeveel liter ijs wilt u?:"))
    for aantal in range(ijsLiter):
        while True:
            SmaakPerLiter = input("Welke smaak wilt u voor liter " + str(aantal + 1) + "?  A) Aardbei, C) Chocolade of V) Vanille?:")
            if SmaakPerLiter in Aardbei or SmaakPerLiter in Chocolade or SmaakPerLiter in Vanille:
                break
            else:
                sorry()



SlagroomPrijs = Slagroom*0.50
SprinkelsPrijs = Sprinkels*0.30*bolletjes
if HoorntjeBakje in hoorntjeLijst:
    CaramelPrijs = Caramel*0.60
elif HoorntjeBakje in bakjeLijst:
    CaramelPrijs = Caramel*0.90
CaramelPrijs = 0

ToppingPrijs = SlagroomPrijs + SprinkelsPrijs + CaramelPrijs


Bolletjes = AantalBolletjes*0.95
Hoorntjes = Hoorntje*1.25
Bakjes = Bakje*0.75
TotaalParticulier = Bolletjes + Hoorntjes + Bakjes + ToppingPrijs

ijsLiterPrijs = ijsLiter*9.80
btw = ijsLiterPrijs*0.06

print("----------[Papi Gelato]----------")
if ParticulierZakelijk in particulierLijst:
    print(f"Bolletjes    {bolletjes} X €0.95  = €{Bolletjes:.2f}")
    if HoorntjeBakje in hoorntjeLijst:
        print(f"Hoorntje     {Hoorntje} X €1,25  = €{Hoorntjes:.2f}")
    else:
        print(f"Bakje         {Bakje} X €0.75 = €{Bakjes:.2f}")

    if Slagroom > 0 or Sprinkels > 0 or Sprinkels > 0 or Caramel > 0:
        print(f"Topping        1 X €{ToppingPrijs:.2f} = €{ToppingPrijs:.2f}")
    print("                         -------- +")
    print(f"                        = €{TotaalParticulier:.2f}")

elif ParticulierZakelijk in zakelijkLijst:
    print(f"Liter   {ijsLiter} X €9.80 = €{ijsLiterPrijs:.2f}")
    print("                         -------- +")
    print(f"Totaal                  = €{ijsLiterPrijs:.2f}")
    print(f"BTW (6%)                 = €{btw:.2f}")

