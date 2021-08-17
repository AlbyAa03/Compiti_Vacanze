import string

def pangramma(frase):
    lettere = []
    for lettera in frase:
        if lettera not in lettere:
            lettere.append(lettera.lower())
    
    for lettera in string.ascii_lowercase:
        if lettera not in lettere:
            print("non è un pangramma")
            return
    print("è un pangramma")
    return           

def main():
    pangramma("The quick brown fox jumps over the lazy dog.")

if __name__ == '__main__':
    main()
    
