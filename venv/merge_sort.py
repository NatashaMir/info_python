#Merge sort

def merge(a, b):
    c = []
    
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
            
    if len(a) == 0:
          c += b
    else:
          c += a
    return c
    
def mergesort(array):
  
  if len(array) <= 1:
    return array
    
  else:
    middle = len(array)//2
    first = mergesort(array[:middle])
    second = mergesort(array[middle:])
    return merge(first, second)
    
alist = [34,56,132,1,76,43,66,23,0]

print(mergesort(alist))
