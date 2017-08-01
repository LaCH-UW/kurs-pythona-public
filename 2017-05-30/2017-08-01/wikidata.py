
import requests
import json
import urllib.parse


if __name__ == '__main__':
    basic_query = 'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={}&language=pl&format=json'
    basic_page = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'
    print(urllib.parse.quote('Douglas Adams'))
    response = requests.get(basic_query.format(urllib.parse.quote('Douglas Adams'))).json()
    for result in response['search']:
        print(json.dumps(result, indent=2))
        url = basic_page.format(result['id'])
        # print(url)
