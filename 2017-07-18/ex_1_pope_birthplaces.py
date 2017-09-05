import json
import time
import logging
import requests
from lxml import html

from collections import namedtuple

POPE_LOGGER = logging.getLogger('Pope')

Pope = namedtuple('Pope', ['no', 'pontificate', 'potrait', 'name', 'personal_name', 'pob', 'age_start_end', 'notes'])

wiki_host = 'https://en.wikipedia.org'


pob_known_json_fname = 'popes_known_coords.json'
pob_unknown_json_fname = 'popes_unknown_coords.json'


class Place(object):
    def __init__(self, short_name, coords):
        self.short_name = short_name
        self.coords = coords
        self.popes = []

    def to_json(self):
        return json.dumps({
            'short_name': self.short_name,
            'coords': self.coords,
            'popes': self.popes
        })

    @staticmethod
    def from_json(json_obj):
        new_object = Place(json_obj['short_name'], json_obj['coords'])
        new_object.popes = json_obj['popes']
        return new_object


def build_objects():
    wikipedia_page = wiki_host + '/wiki/List_of_popes'
    tree = html.fromstring(requests.get(wikipedia_page).content)
    popes = []
    for i in tree.xpath('.//table[@class="wikitable"]//tr[not(td/@colspan="4")]'):
        try:
            tds = i.xpath('./td')
            if len(tds) != 8:
                continue
            popes.append(Pope(*i.xpath('./td')))
        except ValueError:
            print('Could not parse:', ''.join(i.xpath('.//text()')))

    return popes


def get_coords_from_link(link):
    tree = html.fromstring(requests.get(wiki_host + link).content)
    geo = tree.xpath('//*[@id="mw-content-text"]/div/table[contains(@class, "infobox")]'
                     '//span[contains(@class, "geo-dms")]')
    if len(geo) == 0:
        POPE_LOGGER.info('Not found coords in infobox at %s', link)
        return None

    lat, long = geo[0].xpath('.//span')
    assert lat.get('class') == 'latitude'
    assert long.get('class') == 'longitude'
    return ''.join(lat.xpath('.//text()')), ''.join(long.xpath('.//text()'))


def get_places(popes):
    result = dict()
    for pope in popes:
        pope_name = ''.join(pope.name.xpath('.//small//text()'))
        POPE_LOGGER.debug('Parsing POB for %s', pope_name)
        full_pob_name = pope.pob.xpath('.//text()')[0]
        short_pob_name = full_pob_name.split(',')[0]
        first_link = pope.pob.xpath('.//a[not(preceding-sibling::text()) and not(preceding-sibling::*)]')
        coords = None
        if len(first_link) > 0:
            POPE_LOGGER.debug('Getting coords for %s', full_pob_name)
            coords = get_coords_from_link(first_link[0].get('href'))
            time.sleep(0.5)
        if not short_pob_name in result:
            result[short_pob_name] = Place(short_pob_name, coords)

        result[short_pob_name].popes.append(pope_name)

    return result


def dump_to_files(places):
    with open(pob_known_json_fname, 'w') as fp_known:
        with open(pob_unknown_json_fname, 'w') as fp_unknown:
            for short_name, place in places.items():
                if place.coords:
                    fp_known.write(place.to_json())
                    fp_known.write('\n')
                else:
                    fp_unknown.write(place.to_json())
                    fp_unknown.write('\n')


def load_places(fname):
    result = []
    with open(fname) as fp:
        for line in fp:
            result.append(Place.from_json(json.loads(line)))
    return result



if __name__ == '__main__':
    import sys

    POPE_LOGGER.addHandler(logging.StreamHandler(sys.stdout))
    POPE_LOGGER.setLevel(level=logging.DEBUG)

    popes = build_objects()
    places = get_places(popes)
    dump_to_files(places)