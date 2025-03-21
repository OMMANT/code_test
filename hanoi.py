def hanoi(n, start, mid, end):
    if n == 1:
        return [[start, end]]
    else:
        return hanoi(n - 1, start, end, mid) + [[start, end]] + hanoi(n - 1, mid, start, end)

def solution(n):
    return hanoi(n, 1, 2, 3)

n = 4
print(solution(n))