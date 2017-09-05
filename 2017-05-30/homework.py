#!/usr/bin/python3


import requests
import json


# https://mojepanstwo.pl/api/krs

# krs_podmioty.wartosc_kapital_zakladowy


url = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json?conditions[krs_podmioty.forma_prawna_typ_id]=3&limit=1000'

out_name = 'szpit.json'

while url is not None:
    r = requests.get(url)
    json_data = r.json()
    if 'next' in json_data['Links']:
        url = json_data['Links']['next']
    else:
        url = None
    with open(out_name, 'a', encoding='utf-8') as fp:
        for o in json_data['Dataobject']:
            fp.write(json.dumps(o) + '\n')

results = []

with open(out_name) as fp:
    for line in fp:
        results.append(json.loads(line))

cnt = 0
all_cnt = len(results)
for o in results:
    if o['data']['krs_podmioty.dotacje_ue_beneficjent_id'] != '0':
        cnt += 1

print(cnt, all_cnt)


g = results[-1]


