# Problem No.: A
# Solver:      Jinmin Goh
# Date:        20200403

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        nums = list(map(int, sys.stdin.readline().split()))
        numSet = set(nums)
        cnt = 0
        while True:
            if cnt + 1 in numSet:
                cnt += 1
                continue
            else:
                if x == 0:
                    break
                x -= 1
                cnt += 1
        print(cnt)
    return

if __name__ == "__main__":
    main()