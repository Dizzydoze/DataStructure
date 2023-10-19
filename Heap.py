import time


class MaxHeap:
    """
    1. complete binary tree
    2. the value in each internal node >= the values in the children of that node.
    """

    def __init__(self, arr=None):
        if arr:
            # copy the array into data member
            self.__data = arr[:]
            # Heapify, turn Array into Heap
            # find the last Non-Leaf element, which is the parent of the Last Leaf element
            l_non_leaf = self.__parent(self.size() - 1)
            for i in range(l_non_leaf, -1, -1):
                self.__sift_down(i)

        else:
            self.__data = list()

    def size(self):
        """return number of elements in the heap"""
        return len(self.__data)

    def is_empty(self):
        """return whether the heap is empty"""
        return len(self.__data) == 0

    def __parent(self, index):
        """index start from 0, return the parent index of current index in the complete binary tree"""
        if index == 0:  # no parent for root index
            raise Exception("index 0 doesn't have parent.")
        return (index - 1) // 2

    def __left_child(self, index):
        """index start from 0, return the left child index of current index in the complete binary tree"""
        return index * 2 + 1

    def __right_child(self, index):
        """index start from 0, return the right child index of current index in the complete binary tree"""
        return index * 2 + 2

    def add(self, e):
        """add element into maxheap"""
        self.__data.append(e)                     # add new element to the end of the list
        self.__sift_up(len(self.__data) - 1)      # send new element's index to check

    def __sift_up(self, index):
        """compare new element to its parent, ensure value of parent >= value of children"""
        while index > 0 and self.__data[self.__parent(index)] < self.__data[index]:  # index should not be root
            # swap two elements
            self.__data[self.__parent(index)], self.__data[index] = self.__data[index], self.__data[self.__parent(index)]
            # update index
            index = self.__parent(index)

    def find_max(self):
        """find max element in the heap"""
        if self.size() == 0:
            raise Exception("Can not find max when heap is empty.")
        return self.__data[0]

    def extract_max(self):
        """extract max element in the heap"""
        # get max element first
        m = self.find_max()
        # swap max element and last element, the root becomes the smallest element
        self.__data[0], self.__data[self.size() - 1] = self.__data[self.size() - 1], self.__data[0]
        # remove last element
        self.__data.pop()
        # sift down the smallest element
        self.__sift_down(0)

        # return the max element
        return m

    def __sift_down(self, index):
        """move the smallest element downward"""
        # index right_child must be bigger than index left_child
        # loop will end when index left child is out of boundary
        while self.__left_child(index) < self.size():
            # find max_child of current element
            max_idx = self.__left_child(index)
            # right child exists AND right_child is larger
            if max_idx + 1 < self.size() and self.__data[max_idx] < self.__data[max_idx + 1]:
                max_idx += 1
            # current element > bigger child, match definition, sift down ended, break
            if self.__data[index] > self.__data[max_idx]:
                break
            # else we swap the bigger child and current element
            self.__data[index], self.__data[max_idx] = self.__data[max_idx], self.__data[index]
            # update idx to the new swapped position
            index = max_idx

    def replace(self, e):
        """extract max, replace it with a new element"""
        res = self.__data[0]
        # replace the max with new element
        self.__data[0] = e
        # sift down the new element
        self.__sift_down(0)
        return res


def heap_sort_test():
    import random
    n = 100
    max_heap = MaxHeap()
    for _ in range(n):
        max_heap.add(random.randint(1, 100))

    # sort reversely
    res = list()
    for _ in range(1, n):
        res.append(max_heap.extract_max())
    print(res)


def heapify_test(test_data, is_heapify=False):

    start = time.time()

    if is_heapify:
        max_heap = MaxHeap(arr=test_data)
    else:
        max_heap = MaxHeap()
        for i in range(len(test_data)):
            max_heap.add(i)

    end = time.time()
    return end - start


if __name__ == '__main__':
    import random
    arr = [random.randint(0, 100) for _ in range(1000000)]
    heapify_time = heapify_test(arr, is_heapify=True)
    non_heapify_time = heapify_test(arr, is_heapify=False)
    print("Heapify: " + str(heapify_time) + "\n" + "Non-Heapify: " + str(non_heapify_time))
