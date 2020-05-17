# Contest No.: Edu 87
# Problem No.: C2
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq
import math

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        angle = (math.pi * (n // 2 + 1) / (2 * n)) - math.pi / 4
        ans = math.cos(angle)
        for i in range(1, n // 2 + 1):
            ans += math.cos((math.pi / n) * i + angle)
            ans += math.cos((math.pi / n) * i - angle)
        print(ans)
    return

if __name__ == "__main__":
    main()