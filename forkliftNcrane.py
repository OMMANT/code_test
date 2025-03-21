# 순차탐색, BFS/DFS

from collections import deque
def remove_crane(storage, target):
    n, m = len(storage), len(storage[0])

    for i in range(n):
        for j in range(m):
            if storage[i][j] == target:
                storage[i][j] = '\0'

def remove_forklift(storage, target):
    n, m = len(storage), len(storage[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and storage[i][j] == '\0':
                queue.append((i, j))
                visited[i][j] = True

    # 인접한 빈 공간 파악
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and storage[nx][ny] == '\0':
                queue.append((nx, ny))
                visited[nx][ny] = True

    # target 제거
    queue = deque()
    for i in range(n):
        for j in range(m):
            if storage[i][j] == target:
                # 외부에서 접근 가능한가? (인접 구역이 visited라면 외부 접근 가능함)
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if visited[nx][ny]:
                            storage[i][j] = '\0'
                    elif not visited[i][j]:
                        storage[i][j] = '\0'

def solution(storage, requests):
    storage = [list(row) for row in storage]
    n, m = len(storage), len(storage[0])
    for request in requests:
        if len(request) == 1:
            remove_forklift(storage, request)
        elif len(request) == 2:
            remove_crane(storage, request[0])
    answer = 0
    for i in range(n):
        for j in range(m):
            if storage[i][j] != '\0':
                answer += 1

    return answer

storage = [
    ["AZWQY", "CAABX", "BBDDA", "ACACA"],
    ["HAH", "HBH", "HHH", "HAH", "HBH"]
]
requests = [
    ["A", "BB", "A"],
    ["C", "B", "B", "B", "B", "H"]
]

for a, b in zip(storage, requests):
    print(solution(a, b))