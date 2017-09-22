#!/usr/bin/python
import bogo1
import inlined
import random
import sys

TESTS = 500

for _ in range(TESTS):
    for mod in inlined, bogo1:
        lst = [random.randrange(-5,5) for i in range(5)]
        mod.sort(lst)
        if "-v" in sys.argv:
            print(mod.__name__, lst)
        if sorted(lst) != lst:
            sys.exit("Testing failed - {} produced {}".format(mod, lst))
else:
    print("Testing passed")
