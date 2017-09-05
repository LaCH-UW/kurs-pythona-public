
import requests
import logging


def needs_session(foo):
    def decorated_foo(self, *args, **kwargs):
        logging.error('dekorowana funlcja start')
        self.session = requests.session()
        result = foo(self, *args, **kwargs)
        logging.error('dekorowana funlcja end')
        return result

    return decorated_foo

class Downloader:
    session = None

    @needs_session
    def download_sth(self):
        print(self.session)

    def download_other(self):
        print(self.session)

    @needs_session
    def download_parameterized(self, param):
        pass

    def process(self):
        pass



d = Downloader()

d.download_sth()
