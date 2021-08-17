nLibri = 0
libri = []
sconti = [0,5,10,20,25]
costo  = 8
def inserimento():
    global nLibri
    nLibri = int(input("quanti libri vuole comprare?"))
    print('inserire numero dei libri (da uno a 5)')
    for _ in range(nLibri):
        libri.append(int(input()))
        
        
def calcolo():
    tot= 0
    
    while len(libri)!=0:
        diversi = 0
        b = []
        for temp in range(5):
            if temp+1 in libri:
                b.append(libri.remove(temp+1))
                diversi+=1
        tot += diversi*costo - (diversi*costo*sconti[diversi-1]/100)
        
        print(tot)
        
def main():
    inserimento()
    calcolo()

if __name__ == '__main__':
    main()
    
