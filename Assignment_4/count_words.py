def count_words(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    noPunc = ""
    for char in text:
        if char not in punctuations:
            noPunc += char
    lowerCaseString = noPunc.lower()

    dict = {}
    lst = lowerCaseString.split()
    for item in lst:
        if item in dict:
            counting = dict[item]
            counting += 1
            dict[item] = counting
        else:
            dict[item] = 1

    return dict


print(count_words("wow it's Working good wow!! now now ha ha"))