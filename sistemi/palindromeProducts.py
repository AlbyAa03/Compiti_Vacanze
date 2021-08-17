def isPalindromo(num):
    num = str(num)
    for temp in range(len(num)//2):
        if num[temp] != num[len(num)-(temp+1)]: return False        
    return True
def prodottoPalindromo(min, max):
    minimo = [min,max]
    massimo= [min,max]
    possibilita = []
    
    for n1 in range(min,max+1,1):
        for n2 in range(min,max+1,1):
            prod = n1*n2
            if(isPalindromo(prod)):
                possibilita.append(n1*n2)
                if(prod<minimo[0]*minimo[1]):
                    minimo[0] = n1
                    minimo[1] = n2
                if(prod>massimo[0]*massimo[1]):
                    massimo[0] = n1
                    massimo[1] = n2
                
    print(massimo,minimo)
            
            
def main():
    prodottoPalindromo(10,99)
    
    
if __name__ == '__main__':
    main()
    
