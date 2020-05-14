# Contest No.: 642
# Problem No.: A
# Solver:      JEMINI
# Date:        20200514

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(2 * m)
    return

if __name__ == "__main__":
    main()