# Contest No.: 643
# Problem No.: D
# Solver:      JEMINI
# Date:        20200516

import sys
import heapq

def main():
    n, s = map(int, input().split())
    if n == 1:
        if s == 1:
            print("NO")
        else:
            print("YES")
            print(s)
            print(s // 2)
        return
    if n > s // 2:
        print("NO")
        return
    print("YES")
    for i in range(n - 1):
        print(1, end= " ")
    print(s - n + 1)
    print(s - n)
    return

if __name__ == "__main__":
    main()