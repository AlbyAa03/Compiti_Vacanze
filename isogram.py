def isogram(parola):
    p2 = ""
    for lettera in parola:
        if lettera not in p2:
            p2 = p2+ lettera
        else:
            raise Exception(f"{parola} non è un isogramma perchè {lettera} compare più volte")
    return "isogramma"

def main():
    print(isogram("abcdefghijklmnopqrstuvwaxyz"))
    

if __name__ == '__main__':
    main()