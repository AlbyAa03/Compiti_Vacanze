def differenza(n):
    somma = 0
    sommaQuadrati = 0
    
    for num in range(n+1):
        somma += num
        sommaQuadrati += num ** 2
    
    print(abs((somma**2) - sommaQuadrati))


def main():
    differenza(10)

if __name__ == '__main__':
    main()
    
