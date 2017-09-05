from lxml import html
import requests


class HappyCounter():
    def __init__(self):
        self.all_cnt = 0
        self.all_pop = 0
        self.navy_cnt = 0
        self.navy_pop = 0

    def count_navy(self, pop):
        self.navy_cnt += 1
        self.navy_pop += pop
        self._count_any(pop)

    def count_no_navy(self, pop):
        self._count_any(pop)

    def _count_any(self, pop):
        self.all_cnt += 1
        self.all_pop += pop


# if __name__ == '__main__':
landlocked_url = 'https://en.wikipedia.org/wiki/Landlocked_country'
landlocked_navy_url = 'https://en.wikipedia.org/wiki/Navies_of_landlocked_countries'

def get_populations():
    tree = html.fromstring(requests.get(landlocked_url).content)
    countries = []
    for ctry_line in tree.xpath('//*[@id="mw-content-text"]/div/table//tr[td]'):
        name_list = ctry_line.xpath('.//td[1]/a')
        if len(name_list) == 0:
            continue
        name = name_list[0].attrib['title']
        population = int(ctry_line.xpath('.//td[3]/text()')[0].replace(',', ''))
        countries.append((name, population))
    return countries

def izi_mode():
    """ without Turkmenistan """
    with_navy = set()
    tree = html.fromstring(requests.get(landlocked_navy_url).content)
    for ctry_href in tree.xpath('//*[@id="mw-content-text"]/div/ul/li/a[1]'):
        with_navy.add(ctry_href.attrib['title'])
    return with_navy

def hard_mode():
    with_navy = set()
    tree = html.fromstring(requests.get(landlocked_navy_url).content)
    for ctry_line in tree.xpath('//*[@id="mw-content-text"]/div/ul/li'):
        for ctry_href in ctry_line.xpath('.//text()[contains(., "–") or contains(., "-")][1]/preceding-sibling::a'):
            with_navy.add(ctry_href.attrib['title'])
    return with_navy

if __name__ == '__main__':
    pops = get_populations()

    with_navy = izi_mode()
    cnt = HappyCounter()
    for name, pop in pops:
        if name in with_navy:
            cnt.count_navy(pop)
        else:
            cnt.count_no_navy(pop)

    print('{} of {} has navy'.format(cnt.navy_cnt, cnt.all_cnt))
    print('{}% population'.format(cnt.navy_pop / cnt.all_pop))

    with_navy = hard_mode()
    cnt = HappyCounter()
    for name, pop in pops:
        if name in with_navy:
            cnt.count_navy(pop)
        else:
            cnt.count_no_navy(pop)

    print('{} of {} has navy'.format(cnt.navy_cnt, cnt.all_cnt))
    print('{}% population'.format(cnt.navy_pop / cnt.all_pop))
