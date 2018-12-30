def mergesort(sequence):
   if len(sequence) <= 1:
       return sequence[:]
   else:
       mid = len(sequence) // 2

       left = mergesort(sequence[:mid])
       right = mergesort(sequence[mid:])

       return merge(left, right)


def merge(list1, list2):
    sorted = []
    count1, count2 = 0, 0
    while count1 < len( list1 ) and count2 < len( list2 ):
        if list1[count1] < list2[count2]:
            sorted.append( list1[count1] )
            count1 += 1
        else:
            sorted.append( list2[count2] )
            count2 += 1
    sorted += list1[count1:]
    sorted += list2[count2:]
    return sorted
