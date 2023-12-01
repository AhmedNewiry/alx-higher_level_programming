#!/usr/bin/env python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    left = 0
    right = len(list_of_integers) - 1
    while right >= left:
        mid = left + ((right - left) // 2)
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        elif mid < len(list_of_integers) - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
            left = mid + 1
        else:
            return list_of_integers[mid]
