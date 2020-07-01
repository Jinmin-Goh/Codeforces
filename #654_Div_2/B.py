# Contest No.: 654
# Problem No.: B
# Solver:      JEMINI
# Date:        20200701

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, r = map(int, sys.stdin.readline().split())
        val = min(n, r)
        ans = val * (val - 1) // 2
        
        if r >= n:
            print(ans + 1)
        else:
            print(ans + r)
    return

if __name__ == "__main__":
    main()