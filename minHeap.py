class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        # Move the last item to the root and sift down
        self.heap[0] = self.heap.pop()
        print("test",self.heap[0])

        self._sift_down(0)
        return min_value

    def _sift_up(self, index):
        """
        this swaps out the heaps if the child is < than the parent will this 
        """
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    h = MinHeap()
    h.push(5)
    h.push(1)
    h.push(8)
    print(h)        # [1, 5, 8]

    h.push(0)
    h.push(-1)
    print(h)        # 
    print(h.pop())  # -1
    print(h)        # 
    print(h.pop())  # -1
    print(h)        # 

