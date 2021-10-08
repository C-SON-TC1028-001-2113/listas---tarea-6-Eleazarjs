

def main():
    t = int(input(''))
    a = int(input(''))
    s = t*a
    i=0
    lista = []
    while i<s:
        i=i+1
        w = int(input(''))
        if w<10:
            lista.append(w)
    print(lista)


if __name__=='__main__':
    main()
