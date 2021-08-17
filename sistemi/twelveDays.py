frase = "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
giorno = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
regali = ["a Partridge in a Pear Tree","two Turtle Doves","three French Hens","four Calling Birds","five Gold Rings","six Geese-a-Laying","seven Swans-a-Swimming","eight Maids-a-Milking","nine Ladies Dancing","ten Lords-a-Leaping","eleven Pipers Piping","twelve Drummers Drumming"]
def main():
    for day in range(12):
        precedenti = ""
        for passati in range(day,0,-1):
            precedenti = f"{precedenti}, {regali[passati]}"
        e = "and" # AND è già una parola chiave in python
        if(day == 0):
            e = ""
        precedenti = precedenti[1:]
        precedenti = f"{precedenti}, {e} {regali[0]}"
        print(f"On the {giorno[day]} day of Christmas my true love gave to me: {precedenti}.")

if __name__ == '__main__':
    main()
    