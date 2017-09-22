#!/usr/bin/env python3
sort = (lambda repeat=__import__("itertools").repeat, shuffle=__import__("random").shuffle: lambda lst: next(lst for _ in repeat(None) if shuffle(lst) or (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))))()
