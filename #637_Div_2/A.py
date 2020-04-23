# Contest No.: 637
# Problem No.: A
# Solver:      JEMINI
# Date:        20200423

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, sys.stdin.readline().split())
        maxSum = c + d
        minSum = c - d
        maxW = maxSum // n
        minW = minSum // n
        if n * (a - b) > c + d or n * (a + b) < c - d:
            print("No")
        else:
            print("Yes")

    return

if __name__ == "__main__":
    main()