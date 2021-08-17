def eBisestile(anno):
    if(anno % 4 == 0 and anno%100!=0 or anno%400 == 0):
        return "è bisestile"
    return "non è bisestile"

def main():
    anno = int(input("inserire anno"))
    print(eBisestile(anno))

if __name__ == '__main__':
    main()
    
