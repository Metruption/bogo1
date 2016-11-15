#!/usr/bin/python
from random import shuffle
def bogo_sort(lst,patience_value=1000):
	return [lst for i in range(patience_value) if shuffle(lst) != None or all(lst[i] <= lst[i+1] for i in range(len(lst)-1))][0]
