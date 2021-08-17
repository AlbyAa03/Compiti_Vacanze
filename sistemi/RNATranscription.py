CORRISPETTIVO = {"G":"C","C":"G","T":"A","A":"U"}


def trascrittore(DNA):
    try:
        stampa = "" # faccio così sennò inizia a stampare la stringa e poi dice che non era valida.
        for lettera in DNA:
            stampa  += f"{lettera.upper()}->{CORRISPETTIVO[lettera]}\n"
        print(stampa)
    except:
        print(F"{DNA}: STRINGA NON VALIDA")

def main():
    trascrittore("GCTA")
    trascrittore("GCTU")
    

if __name__ == '__main__':
    main()
    
