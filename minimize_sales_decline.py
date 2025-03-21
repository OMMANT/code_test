# 탐색, 자료구조

class Node:
    def __init__(self, id: int, sale: int):
        self.id = id
        self.sale = sale
        self.root = None
        self.children = []
        self.dp = [0, 0]


def solution(sales, links):
    nodes = [Node(0, 0)]
    for i in range(len(sales)):
        nodes.append(Node(i + 1, sales[i]))
    for link in links:
        leader, supporter = link
        nodes[leader].children.append(nodes[supporter])
        nodes[supporter].root = nodes[leader]

    def dfs(node: Node):
        node.dp[0] = 0
        node.dp[1] = node.sale

        if not node.children:
            return
        
        temp = float('inf')
        for child in node.children:
            dfs(child)
            node.dp[1] += min(child.dp[0], child.dp[1])
            if child.dp[0] < child.dp[1]:
                node.dp[0] += child.dp[0]
                temp = min(temp, child.dp[1] - child.dp[0])
            else:
                node.dp[0] += child.dp[1]
                temp = 0
        
        node.dp[0] += temp

    dfs(nodes[1])
    return min(nodes[1].dp[0], nodes[1].dp[1])

sales = [
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [5, 6, 5, 3, 4],
    [5, 6, 5, 1, 4],
    [10, 10, 1, 1]
]
links = [
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
    [[2, 3], [1, 4], [2, 5], [1, 2]],
    [[2, 3], [1, 4], [2, 5], [1, 2]],
    [[3, 2], [4, 3], [1, 4]]
]

for a, b in zip(sales, links):
    print(solution(a, b))