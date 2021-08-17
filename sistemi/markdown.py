def markdown(frase):
    frase = frase.replace("__","<b>")
    frase = frase.replace("_","<i>")
    frase = frase.replace("\n","<br>")
    
    finito = False
    temp = 0
    while not finito:
        if temp == 0:
            frase = frase.replace("__","<b>")
            frase = frase.replace("_","<i>")
            frase = frase.replace("\n","<br>")
            temp =1
        else:        
            frase = frase.replace("__","<\\b>")
            frase = frase.replace("_","<\\i>")
            frase = frase.replace("\n","<br>")
            temp = 0
        if "__" not in frase and "_" not in frase and "\n" not in frase:
            finito =  True
            
    print(frase)
    
def main():
    markdown("__Ciao__\nmi chiamo _alberto_")

if __name__ == '__main__':
    main()
