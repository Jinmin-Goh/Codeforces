# Contest No.: 636
# Problem No.: B
# Solver:      JEMINI
# Date:        20200421

import sys

def main():
    t = int(input())
    for _ in range(t):
        num = int(sys.stdin.readline().strip())
        if num % 4:
            print("NO")
        else:
            print("YES")
            sumVal = 0
            for i in range(num // 2):
                print((i + 1) * 2, end = " ")
                sumVal += (i + 1) * 2
            for i in range(num // 2 - 1):
                print((i + 1) * 2 - 1, end = " ")
                sumVal -= (i + 1) * 2 - 1
            print(sumVal)
    return

if __name__ == "__main__":
    main()