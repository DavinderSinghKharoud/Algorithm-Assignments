# This is a bonus question

def nth_min(lst, n):
    if n <= 1:
        return min(lst)
    else:
        minimum = min(lst)
        maximum = max(lst)
        for index, item in enumerate(lst):
            if item == minimum:
                lst[index] = maximum
                break
        return nth_min(lst, n - 1)






