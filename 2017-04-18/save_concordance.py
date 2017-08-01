import nltk
from nltk.tokenize import word_tokenize
import sys

input_filename = "lalka-tom-pierwszy.txt"
output_filename = "3_Wysocki_1.txt"

with open(input_filename, encoding='UTF-8') as input_file:
    raw_text = input_file.read()
    word_tokens = word_tokenize(raw_text)
    nltk_text = nltk.Text(word_tokens)

with open(output_filename, "w", encoding='UTF-8') as output_file:
    saveout = sys.stdout
    sys.stdout = output_file
    nltk_text.concordance("Wysocki")
    sys.stdout = saveout
    output_file.close()


# wersja z grzebaniem w trzewiach nltk
def save_concordance(self, filename, word, width=75, lines=25):
    """
    Print a concordance for ``word`` with the specified context window.

    :param word: The target word
    :type word: str
    :param width: The width of each line, in characters (default=80)
    :type width: int
    :param lines: The number of lines to display (default=25)
    :type lines: int
    """
    half_width = (width - len(word) - 2) // 2
    context = width // 4  # approx number of words of context

    offsets = self.offsets(word)
    if offsets:
        lines = min(lines, len(offsets))
        print("Saving %s of %s matches" % (lines, len(offsets)))
        with open(filename, "w", encoding='UTF-8') as file:
            for i in offsets:
                if lines <= 0:
                    break
                left = (' ' * half_width +
                        ' '.join(self._tokens[i - context:i]))
                right = ' '.join(self._tokens[i + 1:i + context])
                left = left[-half_width:]
                right = right[:half_width]

                # zamienione print na write
                # print(left, self._tokens[i], right)
                file.write(left + " " + self._tokens[i] + " " + right + "\n")
                lines -= 1
    else:
        print("No matches")


concordance = nltk.ConcordanceIndex(nltk_text.tokens, key=lambda s:s.lower())
save_concordance(concordance, "3_Wysocki_2.txt", "Wysocki")