from Heap import MaxHeap


class PriorityQueue:
    """construct priority queue with max heap"""
    def __init__(self):
        self.__max_heap = MaxHeap()

    def get_size(self):
        return self.__max_heap.size()

    def is_empty(self):
        return self.__max_heap.size() == 0

    def get_front(self):
        """highest priority element in queue, which is the max element in max heap"""
        return self.__max_heap.find_max()

    def enqueue(self, e):
        """add element into priority queue"""
        self.__max_heap.add(e)

    def dequeue(self):
        """extract highest priority element from queue"""
        return self.__max_heap.extract_max()
