# Contest No.: 642
# Problem No.: C
# Solver:      JEMINI
# Date:        20200514

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        if n == 1:
            print(0)
        else:
            ans = 0
            n -= 1
            temp = n
            while n > 0:
                ans += temp * 4
                n -= 2
                temp += n
            print(ans)
    return

if __name__ == "__main__":
    main()