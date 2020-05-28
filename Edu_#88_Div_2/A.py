# Contest No.: Edu 88
# Problem No.: A
# Solver:      JEMINI
# Date:        20200528

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        if n // k >= m:
            print(m)
        else:
            maxVal = max(0, n // k)
            remain = max(m - (n // k), 0)
            div = remain // (k - 1)
            if remain % (k - 1):
                div += 1
            print(maxVal - div)
    return

if __name__ == "__main__":
    main()