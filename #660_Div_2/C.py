# Contest No.: 660
# Problem No.: C
# Solver:      JEMINI
# Date:        20200730

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        pList = list(map(int, sys.stdin.readline().split()))
        hList = list(map(int, sys.stdin.readline().split()))
        graph = {}
        for i in range(n - 1):
            a, b = map(int, sys.stdin.readline().split())
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set([b])
            if b in graph:
                graph[b].add(a)
            else:
                graph[b] = set([a])
        
        for i in range(n):
            pList[i] = [pList[i], 0, 0]

        cnt = n
        
        # find leaf nodes first
        flag = True
        leafSet = set()
        while cnt > 1:
            tempList = []
            for i in graph:
                print(i, cnt, graph)
                if i == 1 and cnt != 1:
                    continue
                if len(graph[i]) == 1:
                    graph[i] = list(graph[i])
                    leafSet.add(i)
                    if hList[i - 1] % 2 != pList[i - 1][0] % 2 or abs(hList[i - 1]) > pList[i - 1][0]:
                        flag = False
                        break
                    else:
                        tempPList = pList[i - 1][:]
                        print(tempPList)
                        tempPList[0] -= pList[i - 1][0]
                        tempPList[1] = (hList[i - 1] + tempPList[0]) // 2
                        tempPList[2] = -(hList[i - 1] - tempPList[0]) // 2
                        print(tempPList)
                        if tempPList[1] < 0 or tempPList[2] < 0:
                            flag = False
                            break
                        pList[graph[i][0] - 1][0] += pList[i - 1][0] + tempPList[0]
                        pList[graph[i][0] - 1][1] += pList[i - 1][1] + tempPList[1]
                        pList[graph[i][0] - 1][2] += pList[i - 1][2] + tempPList[2]
                    graph[graph[i][0]].remove(i)
                    graph[i] = []
                    cnt -= 1
                    tempList.append(i)
            #print(graph)
            print(pList)
            print(hList)
            if not flag:
                break

        for i in tempList:
            pList[0] += pList[i - 1]

        if hList[0] % 2 != pList[0][0] % 2 or abs(hList[0]) > pList[0][0] or hList[0] != pList[0][1] - pList[0][2]:
            flag = False

        if flag:
            print("YES")
        else:
            print("NO")


    return

if __name__ == "__main__":
    main()