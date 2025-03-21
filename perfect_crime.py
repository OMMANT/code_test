from math import inf

def solution(info: list, n, m):
    dp = [[inf] * (m + 1) for _ in range(len(info) + 1)]
    dp[0][0] = 0
    b_trace = 0
    for i in range(len(info)):
        a_trace, b_trace = info[i]
        
        for b in range(m, -1, -1):
            if dp[i][b] < inf: # 이전에 방문함
                # A도둑이 가져가는 경우
                dp[i + 1][b] = min(dp[i + 1][b], dp[i][b] + a_trace)

                if b + b_trace < m:
                    dp[i + 1][b + b_trace] = min(dp[i + 1][b + b_trace], dp[i][b])

        print(f'[{i}]: {dp}')
    answer = min(dp[len(info)][b] for b in range(m))
    if answer >= n:
        return -1

    return answer

infos = [
    [[1, 2], [2, 3], [2, 1]],
    [[1, 2], [2, 3], [2, 1]],
    [[3, 3], [3, 3]],
    [[3, 3], [3, 3]],
]

ns = [4, 1, 7, 6]
ms = [4, 7, 1, 1]

for info, n, m in zip(infos, ns, ms):
    print(solution(info, n, m))