# Contest No.: 632
# Problem No.: C
# Solver:      JEMINI
# Date:        20200409

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 0
    invalidRange = []
    for i in range(n - 1):
        for j in range(nums):
            if nums[i] != 0:
                ans += 1
            else:
                invalidRange.append((j, j + i))
            
    print(ans)
    return

if __name__ == "__main__":
    main()