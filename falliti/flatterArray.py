def deNestifica(struttura):
    returnare = []
    finito =  False
    s = struttura
    print(type(s))
    while not finito:
        print(s)
        print(returnare)
        if len(s)== 0 :
            finito = True
            continue
        if s[0] == None :
            s.pop(0)
            continue
        if type(s[0])== int:
            returnare.append(s.pop(0))
        else:
            if(len(s[0]) == 0):
                s.pop(0)
            else:
                returnare.append(s[0].pop(0))
        

def main():
    deNestifica([1,[2,3,None,4,[4,6]],[None],5])

if __name__ == '__main__':
    main()
    
