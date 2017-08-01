
import json


pob_known_json_fname = 'popes_known_coords.json'


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


def load_places(fname):
    result = []
    with open(fname) as fp:
        for line in fp:
            result.append(Place.from_json(json.loads(line)))
    return result