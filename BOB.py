def risposta(frase):
    if frase == " ":
        return "Fine. Be that way!"
    MAIUSC = False
    MINUSC = False
    DOMANDA = False
    
    if frase[-1] == "?":
        DOMANDA = True
    
    for lettera in frase:
        if lettera.isupper():
            MAIUSC = True
        if lettera.islower():
            MINUSC = True
    
    if MAIUSC and not MINUSC:
        if DOMANDA:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if DOMANDA:
        return "Sure."
    return "Whatever!"
        
            
    


def main():
    print(risposta("How are you?"))
    print(risposta(" YELL AT HIM "))
    print(risposta("HOW ARE U?"))
    print(risposta(" "))
    print(risposta("buona giornata"))

if __name__ == '__main__':
    main()
    
