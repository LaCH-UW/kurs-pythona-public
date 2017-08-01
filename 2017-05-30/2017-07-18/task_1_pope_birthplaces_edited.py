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


def build_pope_tuples():
    wikipedia_page = wiki_host + '/wiki/List_of_popes'
    tree = html.fromstring(requests.get(wikipedia_page).content)
    popes = dict()

    for row in tree.xpath('//table[@class="wikitable"]//tr[(child::td)]'):
    # for row in tree.xpath('//table[@class="wikitable"]//tr[td]'):
        cols = row.xpath('.//td')
        if len(cols) != 8:
            continue
        popes[''.join(cols[3].xpath('.//a//text()'))] = Pope(*cols)

    return popes


def get_coords_from_link(link):
    POPE_LOGGER.debug('Trying to get coordinates from %s', link)
    tree = html.fromstring(requests.get(wiki_host + link).content)

    coords = tree.xpath('.//*[(@id="coordinates") and not (contains(@class, "coord-missing"))]')
    if len(coords) == 0:
        POPE_LOGGER.debug(' No coordinates found :(')
        return None

    lat = coords[0].xpath('.//*[@class="latitude"]')[0].text_content()
    lon = coords[0].xpath('.//*[@class="longitude"]')[0].text_content()

    return lat, lon


def get_places(popes):
    result = dict()
    places_cache = dict()

    for pope_name, pope in popes.items():
        short_pob_name = pope.pob.text_content().split(',')[0]
        POPE_LOGGER.debug('Parsing POB for %s: %s', pope_name, short_pob_name)

        links = pope.pob.xpath('.//a')
        if len(links) > 0:
            first_link = pope.pob.xpath('.//a')[0]
            if first_link.text_content() == short_pob_name and short_pob_name not in places_cache:
                places_cache[short_pob_name] = get_coords_from_link(first_link.get('href'))

    for pope_name, pope in popes.items():
        short_pob_name = pope.pob.text_content().split(',')[0]
        if short_pob_name in places_cache:
            coords = places_cache[short_pob_name]
        else:
            coords = None

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

    popes = build_pope_tuples()
    places = get_places(popes)
    dump_to_files(places)