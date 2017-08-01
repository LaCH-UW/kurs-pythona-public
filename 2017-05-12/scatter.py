from nltk import FreqDist
from matplotlib import pyplot as plt
from matplotlib import rc

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['Wokulski', 'Stanisław', 'Rzecki', 'Izabela', 'Ochocki', 'Łęcki']
title1 = 'lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'


def scatter_plot(x, y, x_line, y_line, names):
    plt.title("Liczba wystąpień słów w Lalce - porównanie tomów")

    # Zarówno na osi x, jak na osi y podanemy dane
    # Im bardziej oddalona wartość od linii, tym większa różnica w częstotliwości występowania pomiędzy tomami
    # Poniżej linii - więcej w tomie I, powyżej - więcej w tomie II
    # (Ale nie jest idealnie wyskalowana)
    plt.scatter(x, y, color='r')
    plt.plot(x_line, y_line, color='b')

    plt.grid()

    # Dodajemy podpisy do punktów
    for label, x_dot, y_dot in zip(names, x, y):
        plt.annotate(label, xy=(x_dot, y_dot), xytext=(x_dot - 10, y_dot + 10))

    plt.tight_layout()
    plt.show()


def count_freq_and_len(fname):
    with open(fname) as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist, len(split_words)


def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(file1, file2, words):
    freq1, len1 = count_freq_and_len(file1)
    freq2, len2 = count_freq_and_len(file2)

    res1 = return_values(freq1, words)
    res2 = return_values(freq2, words)

    # Ustawiamy punkt końcowy wykresu liniowego tak,
    # by w miarę wiernie oddawał proporcje długości tekstów i mieścił się na wykresie
    line1 = [0, len1 / (len1 + len2) * 1200]
    line2 = [0, len2 / (len1 + len2) * 1200]

    scatter_plot(res1, res2, line1, line2, words)


make_plot(title1, title2, words)
