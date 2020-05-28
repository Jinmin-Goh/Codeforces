# Contest No.: Edu 88
# Problem No.: B
# Solver:      JEMINI
# Date:        20200528

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, sys.stdin.readline().split())
        theatre = []
        for i in range(n):
            theatre.append(sys.stdin.readline().strip())
        if 2 * x <= y:
            ans = 0
            for i in range(n):
                for j in range(m):
                    if theatre[i][j] == ".":
                        ans += 1
            print(ans * x)
        else:
            table = []
            twoCnt = 0
            oneCnt = 0
            for i in range(n):
                table.append([])
                for j in range(m):
                    table[-1].append(theatre[i][j])
            for i in range(n):
                for j in range(m):
                    if table[i][j] == ".":
                        if j < m - 1 and table[i][j + 1] == ".":
                            table[i][j] = "*"
                            table[i][j + 1] = "*"
                            twoCnt += 1
                            continue
                        table[i][j] = "*"
                        oneCnt += 1
            print(oneCnt * x + twoCnt * y)
                        
    return

if __name__ == "__main__":
    main()