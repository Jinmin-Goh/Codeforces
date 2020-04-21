# Contest No.: 636
# Problem No.: A
# Solver:      JEMINI
# Date:        20200421

import sys

def main():
    t = int(input())
    for _ in range(t):
        num = int(sys.stdin.readline().strip())
        temp = 3
        cnt = 4
        while num % temp:
            temp += cnt
            cnt <<= 1
        print(num // temp)
    return

if __name__ == "__main__":
    main()