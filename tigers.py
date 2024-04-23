import random
import numpy as np
import matplotlib.pyplot as plt

class Tygrys:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        



    @classmethod
    def generuj_tygrysy(cls):
        tygrysy = []
        xg_lista = []
        yg_lista = []
        t = 0
        for _ in range(20):
                xg = random.uniform(1, 9)  # Zakres od 0 do 100 (można dostosować)
                yg = random.uniform(1, 9)


                wg = random.uniform(0, 2*np.pi)
                k = np.cos(wg)
                l = np.sin(wg)
                x = xg + a 
                y = yg 
                xo, yo = obroc_punkt(x, y, xg, yg, wg)
                tygrys = cls(xo, yo)
                tygrysy.append(tygrys)

                x = xg + a
                y = yg + a
                xo, yo = obroc_punkt(x, y, xg, yg, wg)
                tygrys = cls(xo, yo)
                tygrysy.append(tygrys)

                x = xg - a
                y = yg + a
                xo, yo = obroc_punkt(x, y, xg, yg, wg)
                tygrys = cls(xo, yo)
                tygrysy.append(tygrys)

                x = xg - a
                y = yg
                xo, yo = obroc_punkt(x, y, xg, yg, wg)
                tygrys = cls(xo, yo)
                tygrysy.append(tygrys)

                

                

                x = xg
                y = yg -b
                xo, yo = obroc_punkt(x, y, xg, yg, wg)
                tygrys = cls(xo, yo)
                tygrysy.append(tygrys)

        return tygrysy

def obroc_punkt(x1, y1, x2, y2, wg):
    dx = x2 - x1
    dy = y2 - y1
    x1_n = x2 + (dx * np.cos(wg) - dy * np.sin(wg))
    y1_n = y2 + (dx * np.sin(wg) + dy * np.cos(wg))

    return x1_n, y1_n

def najmniejsze_y(tygrysy): #zwraca index tygrysa o najmniejszym y
    temp = tygrysy[0].y
    temp2 = 0
    for i in range(len(tygrysy)):
        if tygrysy[i].y < temp:
            temp2 = i
            temp = tygrysy[i].y
    return temp2

def oblicz_kat(x1, y1, x2, y2, x3, y3):
    kat =  np.arctan2(y1 - y2, x1 - x2) - np.arctan2(y3 - y2, x3 - x2)
    kat = kat % (np.pi)
    
    if (x3 - x2) * (y2 - y1) == (x2 - x1) * (y3 - y2):
        kat = np.pi

    #stopnie = np.degrees(kat)
    return kat

def drugi_punkt(tygrysy, najmniejsze_y_index):
    x1, y1 = 0, tygrysy[najmniejsze_y_index].y
    najwiekszy_kat = 0
    for i in range(len(tygrysy)):
        if i != najmniejsze_y_index:
            kat = oblicz_kat(x1, y1, tygrysy[najmniejsze_y_index].x, tygrysy[najmniejsze_y_index].y, tygrysy[i].x, tygrysy[i].y)
            if najwiekszy_kat < kat:
                najwiekszy_kat = kat
                index_2 = i
    return index_2

def nastepny_punkt(tygrysy, lista_obwodu_indexy):
    x1, y1 = tygrysy[lista_obwodu_indexy[-2]].x, tygrysy[lista_obwodu_indexy[-2]].y
    x2, y2 = tygrysy[lista_obwodu_indexy[-1]].x, tygrysy[lista_obwodu_indexy[-1]].y
    najwiekszy_kat = 0
    for i in range(len(tygrysy)):
        if i != lista_obwodu_indexy[-1] and i != lista_obwodu_indexy[-2]:
            kat = oblicz_kat(x1, y1, x2, y2, tygrysy[i].x, tygrysy[i].y)
            if najwiekszy_kat < kat:
                najwiekszy_kat = kat
                index_kolejny = i
    return index_kolejny

a = 0.2
b = 0.1
lista_obwodu_indexy = []
tygrysy = Tygrys.generuj_tygrysy()
for tygrys in tygrysy:
    print(f"({tygrys.x}, {tygrys.y})")

najmniejsze_y_index = najmniejsze_y(tygrysy)
print("Najm y: ", najmniejsze_y(tygrysy))
lista_obwodu_indexy.append(najmniejsze_y_index)
lista_obwodu_indexy.append(drugi_punkt(tygrysy, najmniejsze_y_index))

for _ in range(len(tygrysy)):
    kolejny_index = nastepny_punkt(tygrysy, lista_obwodu_indexy)
    if kolejny_index != najmniejsze_y_index:
        lista_obwodu_indexy.append(kolejny_index)
    else:
        break


print("drugi: ", drugi_punkt(tygrysy, najmniejsze_y_index))

#print("N: ", najmniejsze_y(tygrysy), tygrysy[najmniejsze_y(tygrysy)].y)
#print("kat: ", najmniejszy_kat(tygrysy, najmniejsze_y_index))
print("Lista: ", lista_obwodu_indexy)

plt.axis('equal')

for tygrys in tygrysy:
    plt.scatter(tygrys.x, tygrys.y)
for j in range(20):
    for i in range(5*j,5*j+4):
        plt.plot([tygrysy[i].x, tygrysy[i+1].x], [tygrysy[i].y, tygrysy[i+1].y])
    plt.plot([tygrysy[5*j+4].x, tygrysy[5*j].x], [tygrysy[5*j+4].y, tygrysy[5*j].y])

for i in range(len(lista_obwodu_indexy)-1):
    plt.plot([tygrysy[lista_obwodu_indexy[i]].x, tygrysy[lista_obwodu_indexy[i+1]].x], [tygrysy[lista_obwodu_indexy[i]].y, tygrysy[lista_obwodu_indexy[i+1]].y])
plt.plot([tygrysy[lista_obwodu_indexy[0]].x, tygrysy[lista_obwodu_indexy[-1]].x], [tygrysy[lista_obwodu_indexy[0]].y, tygrysy[lista_obwodu_indexy[-1]].y])
plt.show()