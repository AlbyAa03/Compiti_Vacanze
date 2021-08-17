import math


def trovaTerna(num):
    c = 0
    risultati = []
    for a       in range(num-2) :
        for b   in range(1,a):
            c = math.sqrt((float)(a**2 + b**2))
            if (c%1) == 0 and a+b+c==num:
                print(a,b,(int)(c))
                risultati.append([a,b,(int)(c)])
                



def main():
    trovaTerna(12)

if __name__ == '__main__':
    main()
    
