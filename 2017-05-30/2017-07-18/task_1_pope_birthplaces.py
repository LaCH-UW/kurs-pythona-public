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
    popes = []

    # implement me!

    for i in range(0):
        Pope('not', 'really', 'a', 'correct', 'solution', 'to', 'this', 'task')

    return popes


def get_coords_from_link(link):
    POPE_LOGGER.debug('Trying to get coordinates from %s', link)

    # implement me!

    return None


def get_places(popes):
    result = dict()
    for pope in popes:

        # implement me!

        pope_name = 'FILL ME IN'
        POPE_LOGGER.debug('Parsing POB for %s', pope_name)
        short_pob_name = 'ME TOO'
        coords = get_coords_from_link('NOT REALLY A LINK')
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