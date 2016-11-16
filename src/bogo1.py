#!/usr/bin/env python3
from random import shuffle
def sort(lst,patience_value=1000):
    return (list(lst) for n in range(patience_value) if shuffle(lst) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))).__next__()
  
print (sort([4, 5, 6, 1, 2]))
