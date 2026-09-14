handleliste = []

while True:
    print("--- HANDLELISTE ---")
    print("1. Legg til vare")
    print("2. Se handleliste")
    print("3. Fjern vare")
    print("4. Avslutt")
    print("")
    valg = input("Velg: ")

    if valg == "1":
        vare = input("Hva vil du legge til? ")
        handleliste.append(vare)
        print("")
        print("Varen er lagt til")
        print("")

    elif valg == "2":
        for vare in handleliste:
            print(vare)
            print("")

    elif valg == "3":
        vare = input("Hva vil du fjerne? ")

        if vare in handleliste:
            handleliste.remove(vare)
            print("")
            print("Varen er fjernet")
            print("")
        else:
            print("")
            print("Varen finnes ikke.")
            print("")

    elif valg == "4":
        print("Ha det")
        print("")
        break

    else:
        print("Feil valg")
        print("")