"""
@author Tyler C

This is the second part of the second example of my analysis of OOP and FP, showcasing a simple Merge
Sort algorithm, which shows the strengths of FP and
shows weaknesses of OOP
"""
import math
import copy

class MergeSort:

    # nodes for a linked list
    class Node:
        def __init__ (self, left, right, value):
            self.left = left
            self.right = right
            self.value = value

        def __gt__ (self, node):
            return self.value > node.value

        def __lt__ (self, node):
            return self.value < node.value

        def __eq__ (self, node):
            return self.value == node.value

        def __repr__(self):
            return self.value

        def __str__(self):
            return str(self.value)

    # make a linked list out of given list
    def __init__ (self, ls):
        self.first = None
        self.length = len(ls)
        prev = None
        node = None
        for i in ls:
            curr = self.Node(None, None, i)
            if prev is None:
                self.first = curr
            else:
                curr.left = prev
                prev.right = curr
            prev = curr

    def __repr__(self):
        return self.aslist(self.first)

    def __str__(self):
        return str(self.aslist(self.first))

    def mergesort(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return MergeSort([self.first.value])
        
        selfCopy = copy.deepcopy(self)
        secondHalf = self.atindex(math.ceil(self.length/2), self.first)
        prev = secondHalf.left
        prev.right = None
        secondHalf.left = None
        part1 = MergeSort(self.aslist(self.first))
        part2 = MergeSort(self.aslist(secondHalf))
        return MergeSort.sort(part1.mergesort(), part2.mergesort())

    def aslist(self, node):
        if not node:
            return None
        ls = []
        while True:
            ls.append(node.value)
            node = node.right
            if node is None:
                break

        return ls

    def rest(self):
        r = self.first.right
        self.first.right = None
        r.left = None
        return r

    def atindex(self, index, node):
        if index == 0:
            return node
        return self.atindex(index-1, node.right)

    @staticmethod
    def sort(left, right):
        print(left, right)
        if not left:
            if not right:
                return None
            return right
        if left.length == 1:
            if right.length == 1:
                if left.first < right.first:
                    return MergeSort([left.first.value, right.first.value])
                return MergeSort([right.first.value, left.first.value])
            if left.first < right.first:
                return MergeSort([left.first.value] + right.aslist(right.first))
            return MergeSort([right.first.value, left.first.value] + right.aslist(right.rest))
        if not right:
            return left
        if right.length == 1:
            if left.first < right.first:
                return MergeSort([left.first.value, right.first.value] + left.aslist(left.rest()))
            return MergeSort([right.first.value] + left.aslist(left.first))
        if left.first < right.first:
            return MergeSort([left.first.value] + MergeSort.sort(left.rest(), MergeSort(right.aslist(right.first))))
        return MergeSort([right.first.value] + MergeSort.sort(left, MergeSort(right.aslist(right.rest()))).aslist(right.first))


if __name__ == '__main__':
    l = [5, 16, 3, 1, 12]
    ms = MergeSort(l)
    print(ms.aslist(ms.first))
    print(ms.mergesort())
