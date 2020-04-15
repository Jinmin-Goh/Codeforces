# Contest No.: 635
# Problem No.: B
# Solver:      JEMINI
# Date:        20200415

import sys

def main():
    t = int(input())
    for _ in range(t):
        x, n, m = map(int, sys.stdin.readline().split())
        while x > 0 and (n > 0 or m > 0):
            if x > 20:
                if n > 0:
                    x = x // 2 + 10
                    n -= 1
                    continue
                elif m > 0:
                    x -= 10
                    m -= 1
            else:
                if m > 0:
                    x -= 10
                    m -= 1
                else:
                    break
        if x <= 0:
            print("YES")
        else:
            print("NO")
    return

if __name__ == "__main__":
    main()