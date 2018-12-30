def is_sorted(sequence):
    inc,dec,constant=False,False,False

    if len(sequence)<=1:
        return 1
    temp = sequence[0]
    for index in range(1,len(sequence)):
        if temp==sequence[index]:
            constant=True
            temp=sequence[index]
        elif temp<sequence[index]:
            inc=True
            temp=sequence[index]
        elif temp>sequence[index]:
            dec=True
            temp = sequence[index]

    if inc and dec==False:
        return 1
    elif dec and inc==False:
        return -1
    elif constant and inc==False and dec==False:
        return 1
    else:
        return 0
