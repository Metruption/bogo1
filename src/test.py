#!/usr/bin/python
import bogo1
import random
lst = [random.randrange(-5,5) for i in range(5)]
lst = bogo1.sort(lst)
print(lst)