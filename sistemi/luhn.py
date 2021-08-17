def luhn(num):
    try:
        num = str(int(num.replace(" ","")))
    except:
        return "stringa non valida: contiene lettere"
    if (len(num))<2:
        return "Stringa non valida: troppo corto"
    temp = 0
    finito = ""
    for cifra in num[::-1]:
        if temp == 0:
            finito = finito + cifra
            temp = 1
        else:
            a =  int(cifra)*2
            if a >9:
                a = a -9
            finito = finito + str(a)
            temp = 0
    risultato = 0
    for cifra in finito:
        risultato += int(cifra)
    if(risultato%10 == 0):
        return f"{num} è un NUMERO VALIDO"
    return f"{num} è un NUMERO NON VALIDO"
    
        
    #import string
    #print(num.translate({ord(i): None for i in (string.ascii_letters+ " ")}))


def main():
    print(luhn("4539 1488 0343 6467"))
    print(luhn("8273 1232 7352 0569"))

if __name__ == '__main__':
    main()
    
