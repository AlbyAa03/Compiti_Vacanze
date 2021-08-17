def verificatore(ISBN):
    ISBN = ISBN.replace("-","")
    totali =  [int(ISBN[n])*(10-n) if str(ISBN[n]) != 'X' else 10 for n in range(10)  ]
    totale = 0
    for cifra in totali:
        totale+=cifra
    if(totale%11 == 0):
        print("è valido")
    else:
        print("non è valido")
    
    

def main():
    verificatore("3-598-21508-8")
    verificatore("3-598-21508-X")
     

if __name__ == '__main__':
    main()
    
