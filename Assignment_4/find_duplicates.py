def find_duplicates(items1, items2):
    dict = {}
    lst = []
    for item in items1:
        dict[item] = item
    for item in items2:
        if item in dict:
            lst.append(item)
    return lst
