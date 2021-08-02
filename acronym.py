def acronym(parola):
    parole = parola.split(" ")
    acronimo = ""
    for parola in parole:
        acronimo += parola[0].upper() 
    print(acronimo)
    
def main():
    acronym("istituto tecnico industriale statale")
if __name__ == '__main__':
    main()
    
