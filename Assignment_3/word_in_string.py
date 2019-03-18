def word_in_string(word, string):
    if len(word) > len(string):
        return False
    elif word == string[len(string) - len(word) : ]:
        return True
    else:
        return word_in_string(word, string[:-1])

