
def find_duplicates(items1, items2):
    items1=sorted(items1)
    items2=sorted(items2)
    left,right=0,0
    final=[]
    while left<len(items1) and right<len(items2):
        if items1[left]<items2[right]:
            left+=1
        elif items1[left]>items2[right]:
            right+=1
        else:
            final.append(items1[left])
            left+=1
            right+=1
    return final




