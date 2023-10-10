import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def scatter_data(x, y, xlab, ylab, title,cont, color='blue'):
    plt.style.use("seaborn-colorblind")
    fig, ax = plt.subplots()
    #ax.scatter(x, y, color=color)
    ax.scatter(x, y, c=cont)
    ax.set_xticks([6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.set_title(title)
    plt.show()
    # fig.savefig(title+".png")


def scatter_data_both(x1, y1, x2, y2, xlab, ylab, lab1, lab2, title, continuous):
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    ax.scatter(x1, y1, label=lab1, color='blue', alpha=0.5)
    ax.set_xticks([6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.set_title(title)
    ax.scatter(x2, y2, label=lab2, color='red', alpha=0.5)
    #plt.legend()
    plt.show()


ztm_df = pd.DataFrame(pd.read_csv(r"C:\Users\Kuba\PycharmProjects\pythonProject\dane_parsed.csv"))
# print(ztm_df.head())
ztm_useful = ztm_df.iloc[:, [1, 3, 9, 12, 13, 14]]
# ztm_useless=ztm_df.loc[:,['linia','godzina_odczytu','dzien_tygodnia']]
ztm_useful = ztm_useful.sort_values(['godzina_datetime'])
# print(ztm_useless.head())
tram_df = ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'TRAMWAJ']
bus_df = ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'AUTOBUS']
"""scatter_data_both(
    ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'TRAMWAJ']['godzina_f'],
    ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'TRAMWAJ']['opoznienie_f'],
    ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'AUTOBUS']['godzina_f'],
    ztm_useful[ztm_useful['rodzaj_pojazdu'] == 'AUTOBUS']['opoznienie_f'],
    'Godzina pomiaru',
    'Opoźnienie pojazdu',
    'Tramwaje',
    'Autobusy',
    
    'Opoźnienia pojazdów',
    'opoznienie_f'
)"""
print(np.mean(ztm_useful[ztm_useful['linia']==168]['opoznienie_f']))
print(max(ztm_useful[ztm_useful['linia']==168]['opoznienie_f']))
print(min(ztm_useful[ztm_useful['linia']==168]['opoznienie_f']))
scatter_data(
    tram_df['godzina_f'],
    tram_df['opoznienie_f'],
    'Godzina pomiaru',
    'Opóźnienie tramwaju',
    'Opóźnienie tramwaju w zależności od godziny',
    tram_df['linia']
)
# scatter_data(bus_df['godzina_f'],bus_df['opoznienie_f'],'Godzina pomiaru','Opóźnienie autobusu','Opóźnienie autobusu w zależności od godziny','red')
