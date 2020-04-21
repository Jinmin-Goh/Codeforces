# Contest No.: 636
# Problem No.: C
# Solver:      JEMINI
# Date:        20200421

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        negFlag = False
        if nums[0] < 0:
            negFlag = True
        tempVal = nums[0]
        ans = 0
        for i in range(1, n):
            if nums[i] < 0:
                if negFlag:
                    tempVal = max(tempVal, nums[i])
                else:
                    negFlag = True
                    ans += tempVal
                    tempVal = nums[i]
            else:
                if not negFlag:
                    tempVal = max(tempVal, nums[i])
                else:
                    negFlag = False
                    ans += tempVal
                    tempVal = nums[i]
        ans += tempVal
        print(ans)

    return

if __name__ == "__main__":
    main()