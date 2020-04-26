# Contest No.: Edu 86
# Problem No.: A
# Solver:      JEMINI
# Date:        20200426

import sys

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().split())
        a, b = map(int, sys.stdin.readline().split())
        diff = abs(x - y)
        if a * 2 < b:
            ans = (x + y) * a
        else:
            ans = min(x, y) * b + diff * a
        print(ans)
    return

if __name__ == "__main__":
    main()