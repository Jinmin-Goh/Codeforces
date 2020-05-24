# Contest No.: 644
# Problem No.: E
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        table = []
        for i in range(n):
            table.append(sys.stdin.readline().strip())
        visited = set()
        flag = True
        for i in range(n):
            for j in range(n):
                if not flag:
                    break
                if table[i][j] == "0" or (i, j) in visited:
                    continue
                stack = [(i, j)]
                while stack:
                    temp = stack.pop()
                    if temp in visited:
                        continue
                    visited.add(temp)
                    #print(temp)
                    tempFlag = False
                    if temp[0] < n - 1:
                        if table[temp[0] + 1][temp[1]] == "1":
                            tempFlag = True
                            stack.append((temp[0] + 1, temp[1]))
                    if temp[1] < n - 1:
                        if table[temp[0]][temp[1] + 1] == "1":
                            tempFlag = True
                            stack.append((temp[0], temp[1] + 1))
                    if temp[0] == n - 1 or temp[1] == n - 1:
                        tempFlag = True
                    if not tempFlag:
                        flag = False
                        break
                        
            if not flag:
                break
        if flag:
            print("YES")
        else:
            print("NO")

        
        
    return

if __name__ == "__main__":
    main()