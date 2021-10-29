hoorntjeLijst = ["hoorntje", "Hoorntje"]
bakjeLijst = ["bakje", "Bakje"]
Yes = ["Yes", "yes", "Y", "y"]
No = ["No", "no", "N", "n"]

def Sorry():
    print("Sorry dat sanp ik niet...")

# def HoorntjeBakjeDEF():
#     HoorntjeBakje = (input("Wilt u deze " + str(bolletjes) + " in een hoorntje of een bakje? :"))



print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

Begin = True
while Begin:
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    if bolletjes <= 3:
        HoorntjeBakje = (input("Wilt u deze " + str(bolletjes) + " in een hoorntje of een bakje? :"))
        if HoorntjeBakje in hoorntjeLijst or HoorntjeBakje in bakjeLijst:
            Begin = False
        else:
            Sorry()
            Meer = input("Hier is uw " + str(HoorntjeBakje) + " bolletje met " + str(bolletjes) + " bolletjes. Wilt u nog meer bestellen? Y/N :")
            if Meer in Yes:
                Begin = True
            elif Meer in No:
                Begin = False
                print("Bedankt en tot ziens!")
            else:
                Sorry()
    elif bolletjes >= 4 and bolletjes <=8:
        print("test 4-8")
    else:
        Sorry()