# funziona con numeri ad una cifra positivi
mat = [
    [8,4,6],
    [2,7,4],
    [4,3,1]
]

def matrix(matrice):
    print("    ",end="")
    
    for colonna in range(len(matrice[0])):
        print(f"{colonna} ",end="")
        
    print("\n  |-",end="")
    for colonna in range(len(matrice[0])):
        print("--",end="")
    
    numeroRiga = 1
    for riga in matrice:
        print(f"\n{numeroRiga} | ",end="")
        numeroRiga+=1
        for numero in riga:
            print(f"{numero} ",end="")
    
            
        
    
    
def main():
    matrix(mat)

if __name__ == '__main__':
    main()
    