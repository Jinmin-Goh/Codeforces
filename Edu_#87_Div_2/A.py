# Contest No.: Edu 87
# Problem No.: A
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().split())
        a -= b
        ans = 0
        ans += b
        if a > 0 and c <= d:
            print(-1)
            continue
        if a > 0:
            if a % (c - d):
                ans += c * (a // (c - d) + 1)
            else:
                ans += c * (a // (c - d))
        print(ans)
    return

if __name__ == "__main__":
    main()