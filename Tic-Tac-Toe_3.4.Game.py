import random
X = "X"
O = "O"
prazno = " "

print("""
        Dobro dosli u igricu Tic-Tac-Toe!


                   1 | 2 | 3
                  -----------
                   4 | 5 | 6
                  -----------
                   7 | 8 | 9

Ako zelite da igrate prvi pritisnite           1
Ako zelite da racunar igra prvi pritisnite     2

""")
start = True
while start:
    while True:
        try:
            zapocinje_igru = int(input(">"))
            break
        except:
            print("Greska pri unosu!")
            
    if zapocinje_igru == 1:
        covek = X
        kompjuter = O
        start = False
    elif zapocinje_igru == 2:
        kompjuter = X
        covek = O
        start = False
    else:
        print("Unesite 1 ili 2!")

lista = []
for i in range (9):
    lista.append(prazno)

def tabela():
    print("\n\t",lista[0],"|",lista[1], "|",lista[2])
    print("\t-----------")
    print("\t",lista[3],"|",lista[4], "|",lista[5])
    print("\t-----------")
    print("\t",lista[6],"|",lista[7], "|",lista[8])

tabela()
s = 0
a = 0
def pobednik():
    global s, a
    pobeda = ((1,2,3),
              (4,5,6),
              (7,8,9),
              (1,4,7),
              (2,5,8),
              (3,6,9),
              (1,5,9),
              (3,5,7))
    for i in pobeda:
        for j in i:
            if lista[j-1] == X:
                s += 1
                if s == 3:
                    pobednik = X
                    return pobednik
            elif lista[j-1] == O:
                a += 1
                if a == 3:
                    pobednik = O
                    return pobednik
        s = 0
        a = 0
    if prazno not in lista:
        pobednik = "Nereseno"
        return pobednik
    else:
        return None

def dozvoljeni_potezi():
    dozvoljeni_potez = []
    for i in range(9):
        if lista[i] == prazno:
            dozvoljeni_potez.append(i+1)
    print("\nDozvoljeni potezi: ", dozvoljeni_potez)

    return dozvoljeni_potez
    
def covek_igra():
    global dozvoljeni_potez
    potez = True
    while potez:
        
        while True:
            try:
                covekov_potez = int(input("\nUnesite broj polja: ")) -1
                break
            except:
                print("Greska pri unosu!")
                
        if covekov_potez+1 in dozvoljeni_potez:
            lista[covekov_potez] = covek
            potez = False
        else:
            print("\nPolje ne postoji ili je zauzeto, igrajte opet!")
            continue
    return lista[covekov_potez],covekov_potez

pob = None
def racunar_igra():
    global kompjuter,s,a,pob,prazno,covek
    najbolji_potezi = (5,1,3,7,9,2,4,6,8)
    pobeda = ((1,2,3),
              (4,5,6),
              (7,8,9),
              (1,4,7),
              (2,5,8),
              (3,6,9),
              (1,5,9),
              (3,5,7))
    kopija = lista[:]
    
    dozvoljeni_potez = dozvoljeni_potezi()

    # ako ima polje da rac pobedi da stavi tu
    for c in dozvoljeni_potez:
        kopija[c-1] = kompjuter
        
        for i in pobeda:
            for j in i:
                if kopija[j-1] == X:
                    s += 1
                    if s == 3:
                        pob = X
                        if covek == pob:
                            lista[c-1] = kompjuter
                            return lista[c-1]
                elif kopija[j-1] == O:
                    a += 1
                    if a == 3:
                        pob = O
                        if covek == pob:
                            lista[c-1] = kompjuter
                            return lista[c-1]
            
            s = 0
            a = 0
        kopija[c-1] = prazno

    
    # ako ima polje da covek pobedi da ga blokira
    for b in dozvoljeni_potez:
        kopija[b-1] = covek
        
        for i in pobeda:
            for j in i:
                if kopija[j-1] == X:
                    s += 1
                    if s == 3:
                        pob = X
                        if covek == pob:
                            lista[b-1] = kompjuter
                            return lista[b-1]
                
                elif kopija[j-1] == O:
                    a += 1
                    if a == 3:
                        pob = O
                        if covek == pob:
                            lista[b-1] = kompjuter
                            return lista[b-1]
            
            s = 0
            a = 0
        kopija[b-1] = prazno


    # ako ne postoji nijedno od predhodna dva polja,
    # da stavi u polje iz liste najboljih polja
    for f in najbolji_potezi:
        if f in dozvoljeni_potez:
            lista[f-1] = kompjuter
            return lista[f-1]

def start_game():
    global dozvoljeni_potez
    
    while True:
        
        dozvoljeni_potez = dozvoljeni_potezi()
       
        if covek == X:
            if prazno in lista:
                covek_igra()
                if pobednik() == X:
                    tabela()
                    print("\nCestitamo! X je pobedio!")
                    break
                
            if prazno in lista:
                dozvoljeni_potez = dozvoljeni_potezi()
                racunar_igra()
                if pobednik() == O:
                    tabela()
                    print("\nCestitamo! O je pobedio!")
                    break
                
            if prazno not in lista:
                pobednik()
                tabela()
                print("\nRezultat je neresen!")
                break
            
        elif kompjuter == X:
            if prazno in lista:
                racunar_igra()
                tabela()
                if pobednik() == X:
                    print("\nCestitamo! X je pobedio!")
                    break
                    
            if prazno in lista:
                dozvoljeni_potez = dozvoljeni_potezi()
                covek_igra()
                if pobednik() == O:
                    tabela()
                    print("\nCestitamo! O je pobedio!")
                    break
                    
            if prazno not in lista:
                pobednik()
                print("\nRezultat je neresen!")
                break
                    
        tabela()

start_game()

ponovo = True
while ponovo:
    print("""

Ako zelite da ponovite partiju pritisnite:
Da igrate prvi         1
Da igrate drugi        2
Da izadjete iz igre    0

""")

    start = True
    while start:

        while True:
            try:
                zapocinje_igru = int(input(">"))
                break
            except:
                print("Greska pri unosu!")
                
        if zapocinje_igru == 0:
            break
        if zapocinje_igru == 1:
            covek = X
            kompjuter = O
            start = False
        elif zapocinje_igru == 2:
            kompjuter = X
            covek = O
            start = False
        else:
            print("Unesite 0 ,1 ili 2!")

    if zapocinje_igru == 0:
        print("\nIzasli ste iz igre!")
        start = False
        break

    lista = []
    for i in range (9):
        lista.append(prazno)

    tabela()

    start_game()


input()





