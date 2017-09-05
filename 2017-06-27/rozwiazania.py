





# ', '.join(("'" + i.strip() + "'") for i in 'no, pontificate, potrait, name, personal_name, pob, age_start_end, notes'.split(','))



import requests
from lxml import html

from collections import namedtuple


Pope = namedtuple('Pope', ['no', 'pontificate', 'potrait', 'name', 'personal_name', 'pob', 'age_start_end', 'notes'])


tree = html.fromstring(requests.get('https://en.wikipedia.org/wiki/List_of_popes').content)

popes = []

for i in tree.xpath('.//table[@class="wikitable"]//tr[not(td/@colspan="4")]'):
# for i in tree.xpath('.//table[@class="wikitable"]//tr[not(td/@colspan="4")]'):
    try:
        tds = i.xpath('./td')
        if len(tds) != 8:
            continue
        popes.append(Pope(*i.xpath('./td')))
    except ValueError:
        print(''.join(i.xpath('.//text()')))


for pope in popes:
    print(pope.no.xpath('.//text()'))





