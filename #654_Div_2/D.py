# Contest No.: 654
# Problem No.: D
# Solver:      JEMINI
# Date:        20200701

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        ans = 0
        if k % n:
            ans = 2
        ansTable = [[0] * n for _ in range(n)]
        for i in range(k):
            ansTable[i % n][(i % n + i // n) % n] = 1
        
        print(ans)
        for i in range(n):
            for j in range(n):
                print(ansTable[i][j], end = "")
            print("")
    return

if __name__ == "__main__":
    main()