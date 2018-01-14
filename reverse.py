
def reverse(text):
    rev_string = ""
    i = len(text)-1
    while i >= 0:
        rev_string += text[i]
        i -= 1
    return rev_string

def anti_vowel(text):
    new_string = ""
    for i in range(0, len(text)):
        if text[i] != 'a' and text[i] != 'A'  \
            and text[i] != 'e' and text[i] != 'E' \
            and text[i] != 'i' and text[i] != 'I' \
            and text[i] != 'o' and text[i] != 'O'\
            and text[i] != 'u' and text[i] != 'U':
            new_string += text[i]
    return new_string


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    word = word.lower()
    points = 0
    for i in range(len(word)):
        points += int(score[word[i]])
    return points




string = input('Enter a word: ')
print("Here's the word reversed: ", reverse(string))
print("Here's the word with vowels taken out: ", anti_vowel(string))
print("Here's the word's scrabble score: ", scrabble_score(string))