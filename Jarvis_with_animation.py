import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Tygrys:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def generuj_tygrysy(cls):
        tygrysy = []
        for _ in range(20):
            x = random.uniform(0, 10)
            y = random.uniform(0, 10)
            tygrys = cls(x, y)
            tygrysy.append(tygrys)
        return tygrysy

def najmniejsze_y(tygrysy):
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


lista_obwodu_indexy = []
tygrysy = Tygrys.generuj_tygrysy()
# for tygrys in tygrysy:
#     print(f"({tygrys.x}, {tygrys.y})")

fig, ax = plt.subplots()
tyg = ax.scatter([tygrys.x for tygrys in tygrysy], [tygrys.y for tygrys in tygrysy])
linie = [plt.plot([],
                  [])[0]
         for _ in range(len(tygrysy))]

ax.set_aspect('equal')
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

def update(frame):
    for i in range(len(tygrysy)):
        tygrysy[i].x = tygrysy[i].x + random.uniform(-0.1, 0.1)
        tygrysy[i].y = tygrysy[i].y + random.uniform(-0.1, 0.1)
        if tygrysy[i].x < 0:
            tygrysy[i].x = tygrysy[i].x + random.uniform(0, 0.1)
        elif tygrysy[i].x > 10:
            tygrysy[i].x = tygrysy[i].x - random.uniform(0, 0.1)
        if tygrysy[i].y < 0:
            tygrysy[i].y = tygrysy[i].y + random.uniform(0, 0.1)
        elif tygrysy[i].y > 10:
            tygrysy[i].y = tygrysy[i].y - random.uniform(0, 0.1)
    
    tyg.set_offsets(np.column_stack(([tygrysy[i].x for i in range(len(tygrysy))], [tygrysy[i].y for i in range(len(tygrysy))])))

    lista_obwodu_indexy = []
    najmniejsze_y_index = najmniejsze_y(tygrysy)
    lista_obwodu_indexy.append(najmniejsze_y_index)
    lista_obwodu_indexy.append(drugi_punkt(tygrysy, najmniejsze_y_index))

    for _ in range(len(tygrysy)):
        kolejny_index = nastepny_punkt(tygrysy, lista_obwodu_indexy)
        if kolejny_index != najmniejsze_y_index:
            lista_obwodu_indexy.append(kolejny_index)
        else:
            break

    for i in range(len(tygrysy)):
        linie[i].set_data([], [])

    for i in range(len(lista_obwodu_indexy)-1):
        linie[i].set_data([tygrysy[lista_obwodu_indexy[i]].x, tygrysy[lista_obwodu_indexy[i+1]].x], [tygrysy[lista_obwodu_indexy[i]].y, tygrysy[lista_obwodu_indexy[i+1]].y])
    linie[-1].set_data([tygrysy[lista_obwodu_indexy[0]].x, tygrysy[lista_obwodu_indexy[-1]].x], [tygrysy[lista_obwodu_indexy[0]].y, tygrysy[lista_obwodu_indexy[-1]].y])
    return tyg, linie 
ani = FuncAnimation(fig, update, frames=200, interval=10)
plt.show()



