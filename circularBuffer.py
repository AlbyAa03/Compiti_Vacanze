buffer = [None,None,None,None,None,None,None]
posiz  = 0

def aggiungi(elem):
    global posiz
    buffer[posiz] = elem
    posiz = (posiz+1)%7
    print(buffer)

def main():
    for temp in range(30):
        aggiungi(temp)

if __name__ == '__main__':
    main()