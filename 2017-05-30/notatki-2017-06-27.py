
import requests
from lxml import html

# w ramach próby uporządkowania bałaganu terminologicznego:
# <a href="http://example.com">ważna <b>treść</b></a>
# całe powyższe to węzeł (node) html ze znacznikiem (tag) 'a' [skrótowo będę mówił/pisał "węzeł a"], 
#   z atrybutem 'href' o wartości 'http://example.com', mający dwoje dzieci:
#   węzeł tekstowy ('ważna') i węzeł 'b' (który ma z kolei pojedyncze dziecko, węzeł tekstowy 'treść')
# spostrzeżenie: węzły tekstowe nie mogą mieć dzieci

# pobranie zawartości strony
response = requests.get('https://en.wikipedia.org/wiki/Catholic_religious_order')
# przeparsowanie html i zbudowanie drzewa; pod zmienną tree ląduje korzeń drzewa (węzeł ze znacznikiem html); 
#  html.fromstring buduje drzewo ze stringa
tree = html.fromstring(response.content)

# prosta funkcja wypisująca węzły drzewa; ciekawostka: funkcja jest rekurencyjna (woła sama siebie)
#  uwaga: pisząc funkcje rekurencyjne należy być ostrożnym, da się w ten sposób stworzyć program, który nigdy 
#   się nie kończy (prawie, python wysypie się gdy wykryje bardzo-bardzo dużo wywołań rekurencyjnych);
#   tutaj zawsze przechodzimy dokładnie raz po każdym dziecku każdego elementu, więc nie ma tego ryzyka
def describe(t, depth=0):
    print(depth * ' ', t.tag)
    for sub in t:
        describe(sub, depth + 1)

# przypomnienie: funkcja xpath zawsze zwraca listę pasujących węzłów; może ona być pusta (nic nie pasuje);
#  jeśli pasuje jeden element, lista jest jednoelementowa

# wszystkie tabele na stronie ("potomkowie (descendant) korzenia z tagiem table")
tbs = tree.xpath("//table")

# cały tekst zawarty w pierwszej tabeli ("wszystkie węzły tekstowe będące potomkami węzła pod tbl_1")
#  uwaga: kropka na początku xpatha oznacza, że szukamy potomków danego węzła, a nie korzenia drzewa
tbl_1 = tbs[0]
tbl_1.xpath(".//text()")
# "".join woła się na elemencie, którym chce się połączyć argumenty metody .join
print("".join(tree.xpath("//table")[0].xpath(".//text()")))
# warto zauważyć, że jeśli wypiszemy zmienną w konsole bez printa, znaki specjalne nie zostaną zinteretowane
#  -- zobaczymy '\n' zamiast faktycznych złamań wierszy

# ciekawostka na marginesie: print() woła na obiekcie, który dostaje, funkcję str();
#                            wypisywanie w konsoli woła funkcję repr()
#  warto porównać:
print('a\na')
print(str('a\na'))  # funkcjonalnie to samo, co powyżej
print(repr('a\na'))

# wszystkie wiersze (tr, table row) pierwszej tabeli
tree.xpath("//table")[0].xpath(".//tr")
# poniższe niezbyt intuicyjnie zwróci (por. uwaga w linii 34) wszystkie wiersze tabel na całej stronie
tree.xpath("//table")[0].xpath("//tr")

# wszystkie węzły tekstowe pierwszej komówki (td, table data) pierwszego wiersza pierwszej tabeli
# uwaga: xpath numeruje od 1!
tree.xpath("//table")[0].xpath(".//tr[1]/td")[0].xpath(".//text()")

# wypisujemy wszystkie węzły tekstowe z wytłuszczeniem (b, bold) w komórkach wierszy pierwszej tabeli
for i in tree.xpath("//table")[0].xpath(".//tr/td/b/text()"):
    print(i)

# wszystkie komórki (td) takie, że ich dzieckiem jest pogrubienie, w wierszach pierwszej tabeli
tree.xpath("//table[1]//tr/td[b]")
# wszystkie komórki (td) takie, że ich dzieckiem NIE jest pogrubienie, w wierszach pierwszej tabeli
tree.xpath("//table[1]//tr/td[not(b)]")

# uwaga: ponizsze zwróci wiersze, w których ŻADNA komórka nie zawiera pogrubienia jako dziecka
tree.xpath("//table[1]//tr[not(td/b)]")
# ponizsze zwróci wiersze, w których przynajmniej jedna komórka pogrubienia jako dziecko
tree.xpath("//table[1]//tr[td/b]")

# wszystkie wiersze takie, że przynajmniej jedna komórka ma atrybut (por. linia 5nn) 'align' o wartości 'center'
#  atrybuty, jak widać, oznaczamy "małpą"
tree.xpath('//table[1]//tr[td/@align="center"]')

rows = tree.xpath("//table")[0].xpath(".//tr[not(td/b/text())]")
rows[0].xpath("./td") # wszystkie komórki pierwszego wiersza

# rozwinięcie listy i przypisanie elementów do zmiennych ("list unpacking")
#  jeśli będzie ich na liście inna liczba niż dostarczyliśmy zmiennych po lewej stronie, poleci ValueError
off_name, abbr, comm_name = rows[0].xpath("./td")

# rodzice, bedący linkiem (a, anchor), węzłów wyboldowanych
tree.xpath("//b/parent::a") 
# powyższe jest mniej więcej tożsame z "wszytkie linki takie, że ich dzieckiem jest pogrubienie":
tree.xpath("//b[a]")

# przykład na węzły tekstowe
simple_tree = html.fromstring('<span>krótki <b>ważny</b> tekst</span>')
simple_tree.getchildren()  # [<węzeł b>]
simple_tree.xpath('//text()')  # ['krótki ', 'ważny', ' tekst']
simple_tree.xpath('//b/text()')  # ['ważny']
# "poprzedni brat, będący węzłem tekstowym, węzła b"
simple_tree.xpath('//b/preceding-sibling::text()')  # ['krótki ']
# "kolejny brat, będący węzłem tekstowym, węzła b"
simple_tree.xpath('//b/following-sibling::text()')  # [' tekst']

# policzono instytuty (zgodnie z zadaniem)
len(tree.xpath("//table")[0].xpath('.//tr[not(td/@align="center")]'))

