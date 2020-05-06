# Contest No.: 639
# Problem No.: A
# Solver:      JEMINI
# Date:        20200503

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if min(n, m) == 1 or (n == 2 and m == 2):
            print("YES")
        else:
            print("NO")
    return

if __name__ == "__main__":
    main()