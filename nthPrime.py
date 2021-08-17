

def primesimo(num): #alternativa al crivello
    primi = [2]
    for temp in range(num-1):
        tro = False
        tentativo = primi[-1]+1
        while not tro:
            #print(tentativo)
            for primo in primi:
                if tentativo % primo == 0:
                    tentativo +=1
                    break
            else:
                tro = True
        primi.append(tentativo)
    return primi

def main():
    print(primesimo(100))

if __name__ == '__main__':
    main()
    
