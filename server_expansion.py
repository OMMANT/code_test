from collections import deque

def solution(players, m, k):
    answer = 0
    server = 1
    serverQ = deque()
    for idx, player in enumerate(players):
        peek = serverQ[0] if serverQ else (-1, -1)
        if peek[0] == idx: # 서버 반납
            server -= peek[1]
            serverQ.popleft()
        if player >= server * m: # 증설 필요
            need = player // m - server + 1 # 증설해야 하는 서버 개수
            serverQ.append((idx + k, need))
            answer += need
            server += need
    return answer

players = [
    [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],
    [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
]

m = [3, 5, 1]
k = [5, 1, 1]

for a, b, c in zip(players, m, k):
    print(solution(a, b, c))