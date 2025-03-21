from collections import defaultdict
from itertools import combinations

def solution(n, q, ans):
    valid_count = 0

    for secret_code in combinations(range(1, n + 1), 5):
        valid_flag = True
        
        for i in range(len(q)):
            common_elements = len(set(secret_code) & set(q[i]))
            if common_elements != ans[i]:
                valid_flag = False
                break
        
        if valid_flag:
            valid_count += 1

    return valid_count

n = [10, 15]
q = [
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],
    [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
]
ans = [[2, 3, 4, 3, 3], [2, 1, 3, 0, 1]]

for a, b, c in zip(n, q, ans):
    print(solution(a, b, c))

