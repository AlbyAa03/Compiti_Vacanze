def twoFer():
    temp = input()
    if temp == "":
        return "One for you, one for me."
    elif temp == "esci":
        return temp
    return f"One for {temp}, one for me."

def main():
    while True:
        risposta = twoFer()
        if risposta == "esci":
            return 0
        print(risposta)
    
if __name__ == '__main__':
    main()
    