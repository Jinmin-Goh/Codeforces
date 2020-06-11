# Contest No.: Edu89
# Problem No.: A
# Solver:      JEMINI
# Date:        20200611

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        ans = 0
        if a > b:
            a, b = b, a

        if 2 * a <= b:
            print(a)
            continue
        
        div = (2 * a - b) // 3
        ans = div * 2
        a -= div * 3
        b -= div * 3
        if a >= 1:
            ans += b // 2
        
        print(ans)
    return

if __name__ == "__main__":
    main()