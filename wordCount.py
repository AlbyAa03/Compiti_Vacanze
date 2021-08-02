import numpy as np
separatori = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~\n\t"
def wordCount(frase):
    parole = [""]
    cnt = -1
    for lettera in frase:
        cnt+=1
        if lettera not in separatori and cnt<len(frase):
            parole[-1] +=lettera
        
        else:
            parole.append("")
    
    arr = np.array(parole)
    print(set(map(lambda x  : (x , list(arr).count(x)) , arr)))
        
            
    if parole.count(parole[-1])>=1:
        print("presente", parole[-1])
            
def main():
    wordCount("ciao, mi chiamo mi alberto e e e sono Alberto")

if __name__ == '__main__':
    main()
    
