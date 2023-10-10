import csv
from datetime import datetime
def replace_polish_chars(text):
    replacements = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for orig_char, repl_char in replacements.items():
        text = text.replace(orig_char, repl_char)
        text = text.replace(orig_char.upper(), repl_char.upper())
    return text
def get_model(row):
    rodzaj_pojazdu = row['rodzaj_pojazdu']
    nr_boczny = int(row['nr_boczny'])
    if rodzaj_pojazdu == 'TRAMWAJ':
        if nr_boczny in {97, 98, 111, 112, 115, 116, 125, 126, 135, 136, 134, 138, 139, 142, 143, 144, 145, 148, 149,
                         156, 157, 162, 161, 190, 189, 206, 205, 220, 219, 244, 243, 128, 129, 172, 171, 174, 173, 264,
                         263, 290, 291, 298, 299, 310, 311, 312, 313, 314, 315, 324, 325}:
            return 'KONSTAL'
        elif nr_boczny in {903, 904, 907}:
            return 'DUWAG'
        elif nr_boczny in range(501, 515 + 1):
            return 'SIEMENS'
        elif nr_boczny in range(515, 559 + 1):
            return 'SOLARIS'
        elif nr_boczny in range(399, 414 + 1):
            return 'TATRA'
        else:
            return 'MODERTRANS'
    else:
        return 'AUTOBUS'
def get_time(row):
    godzina=row['godzina_odczytu']
    min=int(godzina[-2:])
    hr=int(godzina[:2])
    return hr+min/60
def convert_time(row):
    godzina=row['godzina_odczytu']
    return datetime.strptime(godzina,'%H:%M').time()
with open('dane.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['model']
    fieldnames = fieldnames+['godzina_f']
    fieldnames = fieldnames+['godzina_datetime']
    rows = []
    for row in reader:
        if row['opoznienie/przyspieszenie'].startswith('-'):
            row['opoznienie/przyspieszenie'] = row['opoznienie/przyspieszenie'][:-3]
        row['nastepny_przystanek'] = replace_polish_chars(row['nastepny_przystanek'])
        row['przystanek_koncowy'] = replace_polish_chars(row['przystanek_koncowy'])
        row['dzien_tygodnia']=replace_polish_chars(row['dzien_tygodnia'])
        row['opoznienie_f'] = row['opoznienie_f'].replace('"', '')
        row['godzina_i'] = row['godzina_i'].replace('"', '')
        row['godzina_i'] = row['godzina_i'].replace(',', '.')
        row['opoznienie_f'] = row['opoznienie_f'].replace(',', '.')
        row['model'] = get_model(row)
        row['godzina_f'] = get_time(row)
        row['godzina_datetime']=convert_time(row)
        rows.append(row)
with open('dane_parsed.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
# bardzo cicho pisze ta klawiatura
#
