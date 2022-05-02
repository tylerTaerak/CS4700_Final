"""
@author Tyler C

This is the first part of the second example of
my analysis of OOP and FP, showcasing a simple
Merge Sort algorithm, which greatly showcases the strengths
of Functional Programming, and not so much those of OOP
"""
import math

def mergeSort(ls):
    if not isinstance(ls, list):
        return ls
    if len(ls) == 1:
        return ls
    return sortHelp(mergeSort(ls[:math.ceil(len(ls)/2)]), mergeSort(ls[math.ceil(len(ls)/2):]))

def sortHelp(left, right):
    if not left:
        if not right:
            return None
        return right
    if not isinstance(left, list):
        if not isinstance(right, list):
            if left < right:
                return [left] + [right]
            return [left] + [right]
        if left < right[0]:
            return [left] + right
        return [right[0]] + [left] + [right[1:]]
    if not right:
        return left
    if not isinstance(right, list):
        if left[0] < right:
            return [left[0]] + [right] + [left[1:]]
        return [right] + left
    if left[0] < right[0]:
        return [left[0]] + sortHelp(left[1:], right)
    return [right[0]] + sortHelp(left, right[1:])


if __name__ == '__main__':
    print(mergeSort([5, 16, 3, 1, 12]))
