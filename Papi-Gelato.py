hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

Aardbei = ["Aardbei", "aardbei", "A", "a"]
Chocolade = ["Chocolade", "chocolade", "C", "c"]
Munt = ["Munt", "munt", "M", "m"]
Vanille = ["Vanille", "vanille", "V", "v"]

VraagSmaak = True
Hoorntje = 0
Bakje = 0
AantalBolletjes = 0

Begin = True
while Begin:
    print("Welkom bij Papi Gelato.")
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    AantalBolletjes += bolletjes
    if bolletjes <= 3:        
        for smaak in range(bolletjes):
            VraagSmaak = True
            while VraagSmaak:
                SmaakPerBol = input("Welke smaak wilt u voor bolletje " + str(smaak + 1) + "?  A) Aardbei, C) Chocolade, M) Munt of V) Vanille?:")
                if SmaakPerBol in Aardbei or SmaakPerBol in Chocolade or SmaakPerBol in Munt or SmaakPerBol in Vanille:
                    VraagSmaak = False
                else:
                    print("Sorry dat snap ik niet...")
                    VraagSmaak = True
        
        HoorntjeBakje = (input("Wilt u deze " + str(bolletjes) + " in een hoorntje of een bakje? :"))
        if HoorntjeBakje in hoorntjeLijst or HoorntjeBakje in bakjeLijst:
            Begin = False
            if HoorntjeBakje in hoorntjeLijst:
                Hoorntje += 1
            elif HoorntjeBakje in bakjeLijst:
                Bakje += 1
            Meer = input("Hier is uw " + str(HoorntjeBakje) + " met " + str(bolletjes) + " bolletjes. Wilt u nog meer bestellen? Y/N :")
            if Meer in Yes:
                Begin = True
            elif Meer in No:
                Begin = False
                print("Bedankt en tot ziens!")
            else:   
                print("Sorry dat snap ik niet...")
    elif bolletjes >= 4 and bolletjes <=8:
        Bakje += 1
        HoorntjeBakje = bakjeLijst
        print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes.")
        Begin = False
    elif bolletjes >8:        
        print("Sorry zulke grote bakken hebben wij niet")
        Begin = True
    else:
        print("Sorry dat snap ik niet...")

Bolletjes = AantalBolletjes*1.10
Hoorntjes = Hoorntje*1.25
Bakjes = Bakje*0.75
Totaal = Bolletjes + Hoorntjes + Bakjes

print("----------[Papi Gelato]----------")
print(f"Bolletjes    {bolletjes} X €1.10  = €{Bolletjes:.2f}")
if HoorntjeBakje in hoorntjeLijst:
    print(f"Hoorntje     {Hoorntje} X €1,25  = €{Hoorntjes:.2f}")
else:
    print(f"Bakje         {Bakje} X €0.75 = €{Bakjes:.2f}")

print("                         -------- +")
print(f"                        = €{Totaal}")