def main():
    lista = [0,1]
    m = []
    m1 = [0]
    a=-1
    while a<0:
        a = int(input(''))
        if a==0:
            print(m)
        elif a>0:
            if a==1:
                print(m1)
            elif a==2:
                print(lista)
            elif a>2:
                for x in range(a-2):
                    lista.append(lista[x]+lista[x+1])
                print(lista)


if __name__=='__main__':
    main()
