import numpy as np

def quicksort(array):
  
  less = []
  equal = []
  over = []
  
  if len(array) > 1:
    
    median = np.median(array)
    for x in array:
      if x < median:
        less.append(x)
      elif x > median:
        over.append(x)
      else:
        equal.append(x)
      
    return quicksort(less) + equal + quicksort(over)
  
  else:
    return array
    
array=[100, 4, 5, 12, 4, 5, 6, 7, 3, 1, 15]    

print(quicksort(array))
