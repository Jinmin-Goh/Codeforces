# Contest No.: Edu 87
# Problem No.: C1
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq
import math

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        ans = 1.0
        for i in range(1, n // 2):
            ans += 2.0 * math.cos((math.pi / n) * i)
        print(ans)
    return

if __name__ == "__main__":
    main()