
import os.path
from nltk import FreqDist

import plotly.offline as py
import plotly.graph_objs as go

path_2017_05_12 = '../2017-05-12'


class DataSource(object):
    def __init__(self, title, fname):
        self.title = title
        self.fname = fname
        with open(fname, encoding='utf8') as fp:
            split_words = fp.read().split()
            self._freq_dist = FreqDist(split_words)
            self._length = len(split_words)

    def __len__(self):
        return self._length

    def get_freq(self, w):
        return self._freq_dist[w] if w in self._freq_dist else 0


def plot_lalka():
    words = ['Wokulski', 'Stanisław', 'Rzecki', 'Izabela', 'Ochocki', 'Łęcki']

    file1 = os.path.join(path_2017_05_12, 'lalka-tom-pierwszy.txt')
    file2 = os.path.join(path_2017_05_12, 'lalka-tom-drugi.txt')

    ds1 = DataSource('lalka-tom-pierwszy.txt', file1)
    ds2 = DataSource('lalka-tom-drugi.txt', file2)

    res1 = (ds1.get_freq(w) for w in words)
    res2 = (ds2.get_freq(w) for w in words)

    line1 = [0, len(ds1) / (len(ds1) + len(ds2)) * 1200]
    line2 = [0, len(ds2) / (len(ds1) + len(ds2)) * 1200]

    data = [
        go.Scatter(x=line1, y=line2, showlegend=False)
    ]

    for w, f1, f2 in zip(words, res1, res2):
        data.append(go.Scatter(x=[f1], y=[f2], name=w, mode='markers'))

    py.plot(data)


def plot_diffs():
    words = ['morze', 'Polska', 'sklep', 'wiosna', 'morze', 'dziecko']
    filenames = map(
        lambda f: os.path.join(path_2017_05_12, f),
        ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt", "ziemia-obiecana-tom-pierwszy.txt"]

    )
    titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]

    sources = []
    for fname, title in zip(filenames, titles):
        sources.append(DataSource(title, fname))

    data = []
    for ds in sources:
        data.append(go.Bar(x=words, y=list(ds.get_freq(w) for w in words), name=ds.title))

    layout = go.Layout(barmode='stack')
    figure = go.Figure(data=data)
    # figure = go.Figure(data=data, layout=layout)
    py.plot(figure)


if __name__ == '__main__':
    pass
    # plot_lalka()
    # plot_diffs()