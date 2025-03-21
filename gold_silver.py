# 

def solution(a, b, g, s, w, t):
    def is_possible(T):
        total_gold, total_silver, total_mineral = 0, 0, 0
        
        for i in range(len(t)): # T 시간동안 각 트럭은 몇 번 왕복 가능할까?
            move = (T // (t[i] * 2)) + (1 if T % (t[i] * 2) >= t[i] else 0)
            max_move_weight = w[i] * move
            gold_deliver = min(g[i], max_move_weight)
            silver_deliver = min(s[i], max_move_weight)
            both_deliver = min(g[i] + s[i], max_move_weight)

            total_gold += gold_deliver
            total_silver += silver_deliver
            total_mineral += both_deliver

        return total_gold >= a and total_silver >= b and total_mineral >= a + b
    
    left, right = 0, 10**15

    while left < right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    return left
            
    

a = [10, 90]
b = [10, 500]
g = [[100], [70, 70, 0]]
s = [[100], [0, 0, 500]]
w = [[7], [100, 100, 2]]
t = [[10], [4, 8, 1]]

for alpha, beta, gamma, delta, epsilon, zeta in zip(a, b, g, s, w, t):
    print(solution(alpha, beta, gamma, delta, epsilon, zeta))