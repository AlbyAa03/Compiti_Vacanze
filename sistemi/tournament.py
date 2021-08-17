import csv

'''
db:
squadre = {nome:[partite giocate,vittorie,pareggi,perse,punti],...}
'''
squadre = {}
def leggiFile():
    #with open(os.path.abspath('../sistemi_tpsit/csvVari/risultatiPartita.csv')) as csv_file:
    #non so perchè ma non funziona...
    with open('/home/alberto/Scrivania/COMPITI_VACANZE/sistemi_tpsit/csvVari/risultatiPartita.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for risultati in csv_reader:
            if risultati[0] not in squadre:
                squadre[risultati[0]] = {'partiteGiocate':0,'vittorie':0,'perse':0,'pareggi':0,'punti':0}
            if risultati[1] not in squadre:
               squadre[risultati[1]] = {'partiteGiocate':0,'vittorie':0,'perse':0,'pareggi':0,'punti':0}
                   
            ris = risultati[2]
            squadre[risultati[0]]['partiteGiocate'] +=1
            squadre[risultati[1]]['partiteGiocate'] +=1
            if int(ris[0]) > int(ris[2]):
                squadre[risultati[0]]['vittorie'] +=1
                squadre[risultati[1]]['perse'] +=1
                squadre[risultati[0]]['punti'] +=3    
            elif int(ris[0]) < int(ris[2]):
                squadre[risultati[1]]['vittorie'] +=1
                squadre[risultati[0]]['perse'] +=1
                squadre[risultati[1]]['punti'] +=3
            else:
                squadre[risultati[0]]['pareggi'] +=1
                squadre[risultati[1]]['punti'] +=1
                squadre[risultati[1]]['pareggi'] +=1
                squadre[risultati[0]]['punti'] +=1
                
         
def salvaRisultatiTorneo():
    with open('./risultatiTorneo.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['nome','partiteGiocate','vittorie','pareggi','perse','punti'])

        writer.writeheader()
        for nome in squadre:
            writer.writerow({**squadre[nome],**{'nome': nome}})
            
            
    print("finito")
def main():
    leggiFile()
    salvaRisultatiTorneo()
    

if __name__ == '__main__':
    main()
    
