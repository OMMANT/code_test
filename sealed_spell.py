def solution(n, bans):
    bans.sort(key=lambda x: (len(x), x))
    real_n = n
    for spell in bans:
        if get_spell_index(spell) <= real_n:
            real_n += 1
    
    return get_n_spell(real_n)

def get_spell_index(spell):
    idx = 0
    for char in spell:
        idx *= 26
        idx += ord(char) - ord('a') + 1
    return idx

def get_n_spell(n):
    temp = []
    while n > 0:
        n -= 1 
        character = (n % 26) + ord('a')
        temp.append(chr(character))
        n //= 26
    return ''.join(temp[::-1])

n = [30, 7388, 26]
bans = [
    ["d", "e", "bb", "aa", "ae"],
    ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"],
    ['z', 'aa']
]

for a, b in zip(n, bans):
    print(solution(a, b))
