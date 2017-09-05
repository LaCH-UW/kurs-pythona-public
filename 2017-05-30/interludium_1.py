#!/usr/bin/python3

import logging
import sys


# interludium pierwsze, o logowaniu i (odrobinę) o wyjątkach


def foo_old(a, b):
    print('jestem bardzo rozmowną funkcją')
    print('mam dodać', a, 'oraz', b)
    try:
        result = a + b
        print('udało mi się dodawanie')
        print('zwracam', result)
        return result
    except Exception as e:
        print('ojejku, nie wyszło mi zupełnie:', e)
        #raise e
        return None


def foo_new(a, b):
    logging.debug('jestem bardzo rozmowną funkcją')
    logging.info('mam dodać %s oraz %s', a, b)
    try:
        result = a + b
        logging.debug('udało mi się dodawanie')
        logging.info('zwracam %s', result)
        return result
    except Exception as e:
        logging.error('ojejku, nie wyszło mi zupełnie: %s', e)
        #raise e
        return None


logging.root.addHandler(logging.StreamHandler(sys.stdout))
logging.root.setLevel(level=logging.DEBUG)


use_old = True

if __name__ == '__main__':
    params = [(2, 2), ('para', 'pet'), (2, None)]
    if use_old:
        foo = foo_old
    else:
        foo = foo_new

    for p in params:
        foo(*p)


