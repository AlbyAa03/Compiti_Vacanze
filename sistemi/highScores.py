def highScores(scores):
    massimo = max(scores)
    ultimo = scores[-1]
    migliori = scores.copy()#sennò i valori cambiano globalmente
    migliori.sort()
    return massimo,ultimo,migliori[-3:]

def main():
    scores = [5,7,3,4,1]

    print(highScores(scores))
    
if __name__ == '__main__':
    main()
    