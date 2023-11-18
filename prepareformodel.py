import pandas as pd
import numpy as np
import urllib.request
import geojson

def replace_polish_chars(text):
    replacements = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for orig_char, repl_char in replacements.items():
        text = text.replace(orig_char, repl_char)
        text = text.replace(orig_char.upper(), repl_char.upper())
    return text

df=pd.read_csv('dane_parsed.csv')
print(df)
#nu     liczba_porzadkowa
#Qua       rodzaj_pojazdu
#nu       nr_boczny
#Qua/nu       linia
#przerobic na latitude, longtitude       nastepny_przystanek
#nu       przystanek koncowy
#Y       opoznienie
#nu       godzina_odczytu
#Qua       dzien_tygodnia
#nu       opoznienie_f
#nu       godzina_i
#nu       opoznienie_i
#Qua       przerobic na stary/nowy model
#Qnt       godzina_f
#nu       godzina_datetime
qualitative=['rodzaj_pojazdu','linia','dzien_tygodnia','model']
quantitative=['godzina_f','nastepny_przystanek']

dataset=df[quantitative+qualitative]
print(dataset)

target_url='https://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=cluster'
ztmdata=urllib.request.urlopen(target_url)
geodata=geojson.load(ztmdata)
geodata_features=geodata['features']
#geodata_features=geodata['features'][:]
coords_name=[]
unique_stops=set()
#print(geodata_features)
prev=None
i=0
for feature in geodata_features:
    name=feature['properties']['stop_name']
    name=replace_polish_chars(name)
    if name not in unique_stops:
        coords = feature['geometry']['coordinates']
        coords_name.append({'coords':coords, 'stop_name': name})
        unique_stops.add(name)
        i+=1
#print(geodata_features[:,1])
df_coords_name=pd.DataFrame(coords_name)
#print(df_coords_name)
merged_dataset=pd.merge(dataset,df_coords_name,left_on='nastepny_przystanek',right_on='stop_name',how='left')
merged_dataset=merged_dataset.dropna(subset='stop_name')
merged_dataset.reset_index(drop=True,inplace=True)
merged_dataset[['latitude','longtitude']]=merged_dataset['coords'].apply(pd.Series)
merged_dataset.drop(columns=['coords'], inplace=True)
merged_dataset.drop(columns=['nastepny_przystanek'], inplace=True)
merged_dataset.drop(columns=['stop_name'], inplace=True)
print(merged_dataset)
