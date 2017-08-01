import re

import plotly.offline as py
import plotly.graph_objs as go


from task_1_pope_birthplaces import pob_known_json_fname, load_places


data = []

coord_re = re.compile(r'(\d+)°(?:(\d+)′)?(?:(\d+)″)?(.)')


def convert_coords(wiki_str):
    print(wiki_str)
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

    known_places.sort(key=lambda p: p.short_name)
    for i, place in enumerate(known_places):
        data.append(go.Scattergeo(
            lon=[place.lon],
            lat=[place.lat],
            text='<br>'.join([str(len(place.popes))] + place.popes[:30]),
            marker=dict(
                size=min(30, 5 + len(place.popes)),
                color='rgb(' + str(i * 10 % 255) + ',' + str((100 + i * 10) % 255) + ',150)',
                line=dict(width=0)
            ),
            name=place.short_name,
        ))

    layout = go.Layout(
            title='Birthplaces of (some) popes',
            showlegend=True,
            geo=dict(
                scope='world',
                resolution=50,
                projection=dict(type='mercator'),
                showland=True,
                landcolor='rgb(217, 217, 217)',
                showcountries=False,
                lonaxis=dict(range=[-15.0, 40.0]),
                lataxis=dict(range=[26.0, 71.0]),
            ),
        )

    fig = go.Figure(layout=layout, data=data)
    py.plot(fig, validate=False)
