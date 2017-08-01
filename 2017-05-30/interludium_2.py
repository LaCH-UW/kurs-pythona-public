#!/usr/bin/python3

import logging
import sys
import random


# interludium drugie, o obiektach


def foo(a, b):
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


class Sumator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("zaistniałem!")
        self.suma = 0
        self.licznik = 0

    def dodaj(self, a):
        self.logger.debug('mam dodać sobie %s', a)
        try:
            self.suma += a
            self.licznik += 1
            self.logger.debug('udało mi się dodawanie')
            self.logger.info('wyszło %s', self.suma)
        except Exception as e:
            logging.error('ojejku, nie wyszło mi zupełnie: %s', e)
            raise e


class MegaZaawansowanySumator(Sumator):
    def __init__(self):
        super().__init__()
        self.min = None
        self.max = None

    def dodaj(self, a):
        super(MegaZaawansowanySumator, self).dodaj(a)
        if not self.min or self.min > a:
            self.min = a
        if not self.max or self.max < a:
            self.max = a


handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)-15s : %(name)s : %(message)s'))
logging.root.addHandler(handler)
logging.root.setLevel(level=logging.ERROR)


use_old = False

if __name__ == '__main__':

    if use_old:
        suma_100 = 0
        for i in range(100):
            suma_100 = foo(i, suma_100)

        suma_rand = 0
        for _ in range(100):
            i = random.randint(100, 200)
            suma_rand = foo(i, suma_rand)

        print(suma_100)
        print(suma_rand)

    else:
        suma_100 = Sumator()
        for i in range(100):
            suma_100.dodaj(i)

        suma_rand = Sumator()
        for _ in range(100):
            i = random.randint(100, 200)
            suma_rand.dodaj(i)

        print(suma_100.suma)
        print(suma_rand.suma)



