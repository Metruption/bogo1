#!/usr/bin/python
from random import shuffle
def sort(lst,patience_value=1000):
    return [list(lst) for n in range(patience_value) if (shuffle(lst) == "it will never equal this, but just to be safe" and False) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))][0]