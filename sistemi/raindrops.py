def raindrops():
    try:
        temp = int(input())
    except:
        return "errore"
    parola  = ""
    if (temp %3 == 0):
        parola += "Pling"
    if (temp %5 == 0):
        parola += "Plang"
    if (temp % 7 == 0):
        parola += "Plong"
    return parola

def main():
    while True:
        risposta = raindrops()
        if risposta == "errore":
            print("errore")
            continue
        elif risposta == "esci":
            return 0
        print(risposta)
    
if __name__ == '__main__':
    main()
    