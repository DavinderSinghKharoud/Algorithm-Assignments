def fibonacci_sequence(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        lst=[0,1]
        a,b=0,1
        for element in range(2,n):
            c=a+b
            lst.append( c )
            a=b
            b=c

    return lst

print(fibonacci_sequence(8))