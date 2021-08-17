VALORI = [
    [1000,"M"],
    [500 ,"D"],
    [100 ,"C"],
    [50  ,"L"],
    [10  ,"X"],
    [5   ,"V"],
    [1   ,"I"]
]
SOSTITUTI = {"IIII":"IV","XXXX":"XL","CCCC":"CD"}
def trasforma(decimale):
    romanoLettere = ""
    romanoNumeri  = 0
    for val in range(len(VALORI)):
        finito = False
        while not finito: 
            if romanoNumeri+VALORI[val][0]<= decimale:
                romanoNumeri+=VALORI[val][0]
                romanoLettere += VALORI[val][1]
            else:
                finito = True
    
    for sostit in SOSTITUTI:
        romanoLettere = romanoLettere.replace(sostit,SOSTITUTI[sostit])            
    print(romanoNumeri,romanoLettere)

def main():
    trasforma(99)
    trasforma(1990)
    trasforma(2008)
    trasforma(1)
if __name__ == '__main__':
    main()
    
