# Contest No.: 642
# Problem No.: B
# Solver:      JEMINI
# Date:        20200514

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        a.sort()
        b.sort()
        aPos = 0
        bPos = -1
        while k > 0 and aPos < n and bPos >= -n and a[aPos] < b[bPos]:
            a[aPos], b[bPos] = b[bPos], a[aPos]
            if aPos < n - 1 and a[aPos] >= a[aPos + 1]:
                aPos += 1
            if bPos > -n and b[bPos] <= b[bPos - 1]:
                bPos -= 1
            k -= 1
        print(sum(a))

    return

if __name__ == "__main__":
    main()