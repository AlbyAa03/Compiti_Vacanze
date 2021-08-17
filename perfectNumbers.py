def numeroPerfetto(num: int):
    somma = 0
    for n in range(num//2):
        if num%(n+1) == 0: somma+=n+1

    return  "numero abbondante" if somma > num else "numero carente" if somma<num  else "numero perfetto"
    
def main():
    print(numeroPerfetto(28))
    print(numeroPerfetto(6))
    print(numeroPerfetto(12))
    print(numeroPerfetto(24))
    print(numeroPerfetto(8))
    

if __name__ == '__main__':
    main()
    
