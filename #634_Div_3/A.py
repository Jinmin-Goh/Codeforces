# Contest No.: 634
# Problem No.: A
# Solver:      JEMINI
# Date:        20200413

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        if n <= 2:
            print(0)
        else:
            print((n - 1) // 2)
    return

if __name__ == "__main__":
    main()