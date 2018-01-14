def censor(text, word):
    text_list = text.split()
    for i in range(len(text_list)):
        if(text_list[i]== word):
            text_list[i] = "*" * len(word)
    return " ".join(text_list)

text = input("Enter a phrase: ")
word = input("Enter a censored word: ")

print(censor(text, word))

