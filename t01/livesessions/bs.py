# 9 Sind meine Wörter Anagramme?
# Diese Funktion soll mir sagen, ob meine beiden Wörter Anagramme sind. Allerdings stimmt etwas nicht.
# Hinweis 1: Ein Anagramm ist ein Wort, das durch Umordnen der Buchstaben eines anderen Wortes entsteht, wobei alle Buchstaben genau einmal verwendet werden.
# Hinweis 2: Mach dir keine Sorgen, wenn du nicht jeden Teil dieser Funktion verstehst – versuche, den Fehler im Code zu finden, indem du einige print-Anweisungen hinzufügst.

def are_anagrams(word1, word2):
    word1_chars_sorted = sorted(word1.lower())
    word2_chars_sorted = sorted(word2.lower())
    sorted_word1 = ''.join(word1_chars_sorted)
    sorted_word2 = ''.join(word2_chars_sorted)
    return sorted_word1 == sorted_word2


print(are_anagrams('Silent', 'Listen'))  # should be True, but gives False

