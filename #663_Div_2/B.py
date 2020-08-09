# Contest No.: 663
# Problem No.: B
# Solver:      JEMINI
# Date:        20200809

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        table = []
        for i in range(n):
            table.append(input().strip())
        ans = 0
        for i in range(n - 1):
            if table[i][-1] == "R":
                ans += 1
        for i in range(m - 1):
            if table[-1][i] == "D":
                ans += 1
        print(ans)
        
    return

if __name__ == "__main__":
    main()