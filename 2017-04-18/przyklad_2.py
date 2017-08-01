from matplotlib import pyplot as plt
from matplotlib import rc

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

slowa = ['Wokulski', 'Rzecki', 'subiekt', 'handel', 'sklep']

def wykres_liniowy(data1, data2, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    plt.plot(data1, color='r', label="Dane 1")
    plt.plot(data2, color='b', label="Dane 2")
    plt.legend()

    plt.grid()

    plt.xticks(range(len(names)), names, rotation=90)

    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

# teraz dopisz kod tworzący wykres punktowy zawierający liczbę wystąpień słów z listy
# z punktami różnych kolorów dla pierwszego i drugiego tomu "Lalki"
# dostosuj legendę itp.

# podpowiedź: funkcję plt.plot(y) zastępuje funkcja plt.scatter(x, y)

