from collections import OrderedDict
from collections.abc import Sequence

def permute(l):
    base_pairs = pairs(len(l))
    pair_groups = OrderedDict(((i,tuple((j,k) for j,k in base_pairs if j == i)) for i, _ in base_pairs))
    selectors = []


def pairs(size):
    return [(i, j) for i in reversed(range(size)) for j in range(size) if i < j]


def swapped(lst, swaps):
    result = list(lst)
    for i_l, i_r in swaps:
        result[i_l], result[i_r] = result[i_r], result[i_l]
    return result


class Permutation(object):
    def __init__(self, items):
        self.items = tuple(items)
    def pairs(self):
        size = len(self.items)
        return [(i, j) for i in reversed(range(size)) for j in range(size) if i <= j]
    def grouped_pairs(self):
        return OrderedDict(((i,tuple((j,k) for j,k in self.pairs() if j == i)) for i in sorted(list(set(self.pairs()))))).keys()
    def swap(self, swap, *args):
        swapped = list(self.items)
        if isinstance(swap, Sequence) and len(swap) == 2:
            i, j = swap
        elif len(args) > 0:
            i, j = swap, args[0]
        else:
            raise Error('Swapping requires two indices for the slots to be exchanged')
        swapped[i],swapped[j] = swapped[j],swapped[i]
        return Permutation(swapped)
    def compute(self):
        pass


def heap(lst, k=None):
    if k is None:
        k = len(lst) - 1
    if k < 2:
        return lst
    heap(lst, k-1)

    for i in range(k-1):
        if k % 2 == 0:
            lst[i], lst[k-1] = lst[k-1], lst[i]
        else:
            lst[0], lst[k-1] = lst[k-1], lst[0]
        heap(lst, k-1)

    return lst


def heapSwap(lst, k=1, swaps=None):
    if swaps is None:
        swaps = [[]]
    if k < 2:
        print(lst, swaps[-1], (len(swaps)-1)%2)
        swaps.append([])
        return
    heapSwap(lst, k-1, swaps)

    for i in range(k-1):
        j = 0
        if k % 2 == 0:
            j = i
        swaps[-1].append((j, k-1))
        lst[j], lst[k-1] = lst[k-1], lst[j]
        heapSwap(lst, k-1, swaps)
    return
