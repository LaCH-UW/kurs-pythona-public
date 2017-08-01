
import re

from pope_helper import pob_known_json_fname, load_places


coord_re_str = r'(\d+)°(?:(\d+)′)?(?:(\d+)″)?(.)'
coord_re = re.compile(coord_re_str)


def convert_coords(wiki_str):
    m = coord_re.match(wiki_str)
    assert m
    deg, min, sec, card = m.groups()
    if min:
        min = float(min)
    else:
        min = 0
    if sec:
        sec = float(sec)
    else:
        sec = 0
    deg = float(deg) + (min / 60) + (sec / 3600)
    if card in ('W', 'S'):
        deg = -deg

    return deg


if __name__ == '__main__':
    known_places = load_places(pob_known_json_fname)

    for place in known_places:
        place.lat = convert_coords(place.coords[0])
        place.lon = convert_coords(place.coords[1])

