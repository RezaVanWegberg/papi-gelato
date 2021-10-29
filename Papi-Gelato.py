hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

Begin = True
while Begin:
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    if bolletjes <= 3:
        HoorntjeBakje = (input("Wilt u deze " + str(bolletjes) + " in een hoorntje of een bakje? :"))
        if HoorntjeBakje in hoorntjeLijst or HoorntjeBakje in bakjeLijst:
            Begin = False
            Meer = input("Hier is uw " + str(HoorntjeBakje) + " bolletje met " + str(bolletjes) + " bolletjes. Wilt u nog meer bestellen? Y/N :")
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