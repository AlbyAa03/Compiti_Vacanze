VALORI = [["gatti",128],["polline",64],["cioccolato",32],["pomodori",16],["fragole",8],["crostacei",4],["arachidi",2],["uova",1]]
#VALORI = [['uova', 1], ['arachidi', 2], ['crostacei', 4], ['fragole', 8], ['pomodori', 16], ['cioccolato', 32], ['polline', 64], ['gatti', 128]]


def allergie(n):
    returnare = []
    somma = 0
    for a in VALORI:
        if n >= a[1]+somma:
            somma += a[1]
            returnare.append(a[0])
    return returnare    
    
def main():
    print(allergie(34))
    print(allergie(127))

if __name__ == '__main__':
    main()
    
