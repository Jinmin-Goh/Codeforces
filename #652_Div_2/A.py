# Contest No.: 652
# Problem No.: A
# Solver:      JEMINI
# Date:        20200623

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 4:
            print("NO")
        else:
            print("YES")
    return

if __name__ == "__main__":
    main()