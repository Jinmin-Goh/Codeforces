# Contest No.: Edu 85
# Problem No.: B
# Solver:      JEMINI
# Date:        20200410

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        nums.sort()
        sumVal = sum(nums)
        ans = n
        for i in nums:
            if sumVal / ans >= x:
                break
            sumVal -= i
            ans -= 1
        print(ans)
    return

if __name__ == "__main__":
    main()