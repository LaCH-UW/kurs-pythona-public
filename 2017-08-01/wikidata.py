

from pope_helper import pob_known_json_fname, load_places



places = load_places(pob_known_json_fname)


print(places[0].to_json())



# places.sort(key=lambda place: place.short_name)
places.sort()

print(places[0] >= places[1])


print(places[0].to_json())


# print(key_retriever(places[0]))