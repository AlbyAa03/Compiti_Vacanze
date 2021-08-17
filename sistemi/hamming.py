def hamming(dna1,dna2):
    if(len(dna1) != len(dna2)):
        return -1
    
    print(f"{dna1}\n{dna2}")
    distanza = 0
    for num in range(len(dna1)):
        if(dna1[num] != dna2[num]):
            distanza+= 1
            print("^",end="")
        else:
            print(" ",end="")
            
    return f"distanza di Hamming: {distanza}"

def main():
    dna1 = "GAGCCTACTAACGGGAT"
    dna2 = "CATCGTAATGACGGCCT"
    print(f"\n{hamming(dna1,dna2)}")
if __name__ == '__main__':
    main()
    
