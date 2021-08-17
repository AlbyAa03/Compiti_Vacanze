#def inserimento(scelta):

registro = {
    "Alberto":5,
    "Luigi": 3,
    "Enrico":1
}

def aggiungi():
    nome = str(input("inserire nome"))
    if nome in registro:
        aggiungi()
        return
    
    classe = int(input("inserire classe"))
    while classe>5 or classe<0:
        classe = int(input("inserire classe"))
    registro[nome] = classe
    print(registro)
    
def elencoPerClasse(classe = -1,ret = False):
    if(classe==-1):
        classe = int(input("inserire classe desiderata"))
        if classe>5 or classe<0:
            elencoPerClasse()
            return
    
    stampa = ""
    for alunno in registro:
        if classe == registro[alunno]:
            stampa = f"{stampa}, {alunno}"

    
    if len(stampa)==0:
        stampa = f"nessuno frequenta la {classe}°"
    else:
        stampa = stampa[1:]
    if ret:
        return stampa
    print(stampa)      
    
def elencoCompleto():
    for anno in range(1,6):
        print(f"Grado {anno}: {elencoPerClasse(classe=anno,ret=True)}.")



def main():
    print("""
        scelte disponibili:
        1 -> aggiungi studente all'elenco delle classi
        2 -> stampare l'elenco completo studenti di una classe
        3 -> stampare l'elenco di tutti gli studenti per classe
        4 -> esci 
        """)
    
    while True:
        scelta = int(input("inserire Scelta: "))    
        if scelta == 1:
            aggiungi()
        elif scelta == 2:
            elencoPerClasse()
        elif scelta == 3:
            elencoCompleto()
        elif scelta == 4:
            break
        else:
            pass
        
            print(scelta)
        

if __name__ == '__main__':
    main()
    
