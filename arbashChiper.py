import string

def cripta(parola: str):
    modificata = ""
    try:
            
        for lettera in parola:
            if len(modificata)%6 == 0: modificata+= " " 
            modificata += string.ascii_lowercase[25-string.ascii_lowercase.find(lettera)]   
    except:
        print("presenti caratteri non validi...")  
        return  

    return modificata



def decripta(parola: str):
    parola = parola.replace(" ","")
    modificata = ""
    for lettera in parola:
        modificata += string.ascii_lowercase[25-string.ascii_lowercase.find(lettera)]   
    return modificata

def main():
    parolaCriptata = cripta("thequickbrownfoxjumpsoverthelazydog")
    parolaDecriptata = decripta(parolaCriptata)
    print(f"{parolaCriptata} = {parolaDecriptata}")


if __name__ == '__main__':
    main()