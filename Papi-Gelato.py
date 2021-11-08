hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

Aardbei = ["Aardbei", "aardbei", "A", "a"]
Chocolade = ["Chocolade", "chocolade", "C", "c"]
Munt = ["Munt", "munt", "M", "m"]
Vanille = ["Vanille", "vanille", "V", "v"]

VraagSmaak = True
# VraagZmaak = 0

Begin = True
while Begin:
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
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
            Meer = input("Hier is uw " + str(HoorntjeBakje) + " met " + str(bolletjes) + " bolletjes. Wilt u nog meer bestellen? Y/N :")
            if Meer in Yes:
                Begin = True
            elif Meer in No:
                Begin = False
                print("Bedankt en tot ziens!")
            else:   
                print("Sorry dat sanp ik niet...")
        elif bolletjes >= 4 and bolletjes <=8:
            print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes.")
            Begin = False
        else:
            print("Sorry zulke grote bakken hebben wij niet")
            Begin = True