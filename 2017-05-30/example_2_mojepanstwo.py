
import requests
import json
import time

r = requests.get('https://api-v3.mojepanstwo.pl/dane/krs_formy_prawne.json')

json_data = r.json()

# print(json_data.keys())

dane = json_data['Dataobject']

# print(dane[0].keys())

#for i in dane:
#    print(i['id'], i['data']['krs_formy_prawne.nazwa'])

id_kolka_rolniczego = NotImplemented()

lista_kolek_rolniczych = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}'.format(id_kolka_rolniczego)

def get_registration_date(link):
    dane = json_data['Dataobject']
    # print(dane[0].keys())

r = requests.get(lista_kolek_rolniczych)
json_data = r.json()
# json_data['Count']
# json_data['Links'].keys()

lista_kolek_rolniczych_po_500 = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_id]={}&limit=500'.format(id_kolka_rolniczego)

# print(dane[0].keys())
def dump_all_pages(first_page_link, fname):
    current_link = first_page_link
    while current_link is not None:
        r = requests.get(current_link)
        print("getting: ", current_link)
        json_data = r.json()
        with open(fname, 'a', encoding='utf-8') as fp:
            for obj in json_data['Dataobject']:
                fp.write(json.dumps(obj) + '\n')
        current_link = json_data['Links']['next'] if 'next' in json_data['Links'] else None
        time.sleep(1)

plik_wynikowy = 'krs.json'

# dump_all_pages(lista_kolek_rolniczych_po_500, plik_wynikowy)

all_elements = []
with open(plik_wynikowy, encoding='utf-8') as fp:
    for line in fp:
        obj = json.loads(line)
        all_elements.append(obj)

# print(all_elements[0]['data'].keys())
# print(list(i for i in all_elements[0]['data'].keys() if ('data' in i)))

klucz_daty_rejestracji = 'nie wiem'

all_elements.sort(key=lambda o: o['data'][klucz_daty_rejestracji])
print(all_elements[0]['slug'], all_elements[0]['data'][klucz_daty_rejestracji])
