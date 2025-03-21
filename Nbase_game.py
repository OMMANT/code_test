def n_base_number(number, base):
    if number == 0:
        return ['0']
    temp = []
    while number > 0:
        leftover = number % base
        if leftover >= 10:
            leftover = chr(leftover - 10 + ord('A'))
        temp.append(leftover)
        number //= base
    return list(map(str, temp[::-1]))

def solution(n, t, m, p):
    text = []
    number = 0
    
    while len(text) < t * m:
        text += n_base_number(number, n)
        number += 1
    return ''.join(text[p - 1:t * m:m])

n = [2, 16, 16]
t = [4, 16, 16]
m = [2, 2, 2]
p = [1, 1, 2]

for a, b, c, d in zip(n, t, m, p):
    print(solution(a, b, c, d))