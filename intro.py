import random
#gjette spill
rettTall = random.randint(0, 1000)

#10forsøk 
for x in range (10):
    gjett = int(input("gjett et tall mellom 0 og 1000: "))
    if gjett == rettTall:
        print("yay")
        break
    elif gjett < rettTall:
        print("høyere!")
    else:
        print("lavere!")
    print("du har", 9 - x, "forsøk igjenn")