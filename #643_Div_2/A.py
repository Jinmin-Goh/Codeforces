# Contest No.: 643
# Problem No.: A
# Solver:      JEMINI
# Date:        20200516

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        if k == 1:
            print(n)
            continue
        else:
            ans = n
            while k > 1 and not (int(min(str(ans))) == 0):
                ans = ans + int(min(str(ans))) * int(max(str(ans)))
                k -= 1
            print(ans)
    return

if __name__ == "__main__":
    main()