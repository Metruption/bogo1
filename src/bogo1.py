#!/usr/bin/env python3
from random import shuffle
from itertools import repeat
def sort(lst):
    return next(lst for _ in repeat(None) if shuffle(lst) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1))))
