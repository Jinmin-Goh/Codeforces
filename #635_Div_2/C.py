# Contest No.: 635
# Problem No.: C
# Solver:      JEMINI
# Date:        20200416

import sys

def main():
    n, k = map(int, input().split())
    graph = {}
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    # bfs, count the leaf nodes and depth
    visited = set([1])
    temp = [1]
    cnt = 1
    costList = []
    while temp:
        nextList = []
        for i in temp:
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    nextList.append(j)
            costList.append(cnt - 1 - (len(graph[i]) - 1))
        cnt += 1
        temp = nextList[:]
    costList.sort()
    print(costList)
    ans = 0
    
    for i in range(k):
        ans += costList[-i - 1]
    print(ans)

    return

if __name__ == "__main__":
    main()