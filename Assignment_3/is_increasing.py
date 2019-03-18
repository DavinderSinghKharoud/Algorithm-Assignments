def is_increasing(lst):
    if not lst:
        return True
    else:
        length=len(lst)
        if lst[length-2]<=lst[length-1]:
            check=is_increasing(lst[:length-1])
            return check
    return False
