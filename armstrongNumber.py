def armstrong(numero):
    somma = 0
    cifre = len(str(numero))
    for cifra in str(numero):
        somma += int(cifra) ** cifre
    if somma == numero:
        print("è un numero di Armstrong")
    else:
        print("non è un numero di Armstrong")

def main():
    armstrong(9)
    armstrong(153)
    armstrong(154)

if __name__ == '__main__':
    main()
    
