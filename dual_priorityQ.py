# 자료구조, 힙, 우선순위큐
import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    for op in operations:
        cmd, n = op.split()
        if cmd == 'I':
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        elif n == '1':
            if max_heap:
                val = heapq.heappop(max_heap)
                min_heap.remove(-val)
                heapq.heapify(min_heap)
        else:
            if min_heap:
                val = heapq.heappop(min_heap)
                max_heap.remove(-val)
                heapq.heapify(max_heap)
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] if max_heap else [0, 0]


operations = [
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
]

for alpha in operations:
    print(solution(alpha))
