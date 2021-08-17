def RLE(frase):
    consecutivi = 0
    precedente = frase[0]
    for lettera in frase:
        if precedente == lettera:
            consecutivi+=1
        else:
            print(f"{consecutivi}{precedente}",end="")
            consecutivi = 1
            precedente = lettera
    if consecutivi == 1:
        print(f"1{frase[-1]}")

def main():
    RLE("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
    

if __name__ == '__main__':
    main()
    
