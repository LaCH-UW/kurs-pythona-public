from nltk import FreqDist
from matplotlib import pyplot as plt
from matplotlib import rc

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['morze', 'Polska', 'sklep', 'wiosna', 'morze', 'dziecko']
filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
             "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]


def heatmap_plot(values, titles, words):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    # Ponownie nazywamy ticks - oś y to tytuły, oś x to słowa
    # Pierwszy parametr to skala danej osi - gdzie mają być punkty na niej
    # Drugi parametr to po prostu etykiety na wcześniej ustawione punkty

    # Dodajemy 0.5, aby wypośrodkować podpisy (są one rozstawione co 1)
    # Można zobaczyć jak wygląda wykres bez dodawania 0.5
    plt.xticks([x + 0.5 for x in range(len(words))], words, rotation=90)
    plt.yticks([x + 0.5 for x in range(len(titles))], titles)

    # Jedynym koniecznym parametrem jest nasza macierz wartości
    plt.pcolor(values)
    plt.tight_layout()
    plt.show()


def count_freq(fname):
    with open(fname) as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist


def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(filenames, titles, words):
    values_matrix = []

    # Tworzymy macierz, która w każdym rzędzie ma liczbę wystąpień naszego zestawu słów dla danego tekstu
    # Kolumny - słowa
    # Rzędy - teksty

    # Macierz to lista list (każda lista na głównej liście to jeden rząd)

    for file in filenames:
        freq = count_freq(file)
        values_matrix.append(return_values(freq, words))

    heatmap_plot(values_matrix, words, titles)


make_plot(filenames, titles, words)
