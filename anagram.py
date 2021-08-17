def anagramma(parola,possibilita):
    returnare = []
    
    for poss in possibilita:
        p = poss
        for lettera in parola:
            if lettera not in p:
                break
            else:
                p = p.replace(lettera,"",1)
                
        else:
            if p == "":
                returnare.append(poss)
                
    return returnare
    


def main():
    print(anagramma("ciao",["oiac","hey","caio","cai","caaio"]))

if __name__ == '__main__':
    main()
    
