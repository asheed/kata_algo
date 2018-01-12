#!/usr/bin/env python
# -*- coding: utf8 -*

def first_non_consecutive(arr):
    for i, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8]):
        if i >= 1 and arr[i + 1] - arr[i] != 1:
            return arr[i+1]
    return None


print(first_non_consecutive([1,2,3,4,6,7,8]))