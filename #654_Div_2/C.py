# Contest No.: 654
# Problem No.: C
# Solver:      JEMINI
# Date:        20200701

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        a, b, n, m = map(int, sys.stdin.readline().split())
        if n + m > a + b:
            print("No")
            continue
        
        if min(a, b) >= m:
            print("Yes")
            continue
        
        diff = abs(a - b)
        
        if diff > n:
            print("No")
            continue
        else:
            minAB = min(a, b)
            a = minAB
            b = minAB
            n -= diff
            # currently min(a, b), min(a, b) for v, c
            minNM = min(n, m)
            a -= minNM
            b -= minNM
            n -= minNM
            m -= minNM
            if m > min(a, b):
                print("No")
            else:
                print("Yes")
    return

if __name__ == "__main__":
    main()