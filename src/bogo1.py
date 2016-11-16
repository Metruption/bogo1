#!/usr/bin/env python3
from random import shuffle
import sys
def sort(lst):
    return (list(lst) for n in range(sys.maxsize) if shuffle(lst) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))).__next__()