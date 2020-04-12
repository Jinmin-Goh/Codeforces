# Contest No.: 633
# Problem No.: B
# Solver:      JEMINI
# Date:        20200412

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        nums.sort()
        ans = []
        leftFlag = None
        pos = None
        if n % 2:
            ans.append(nums[n // 2])
            pos = n // 2
            if abs(nums[n // 2] - nums[n // 2 + 1]) > abs(nums[n // 2] - nums[n // 2 - 1]):
                leftFlag = True
            else:
                leftFlag = False
        else:
            if abs(nums[n // 2] - nums[n // 2 + 1]) > abs(nums[n // 2 - 1] - nums[n // 2 - 2]):
                ans.append(nums[n // 2 - 1])
                pos = n // 2 - 1
                leftFlag = False
            else:
                ans.append(nums[n // 2])
                pos = n // 2
                leftFlag = True
        cnt = 1
        while cnt < n:
            if leftFlag:
                #print(nums[pos - cnt])
                ans.append(nums[pos - cnt])
                pos -= cnt
            else:
                #print(nums[pos + cnt])
                ans.append(nums[pos + cnt])
                pos += cnt
            leftFlag = not leftFlag
            cnt += 1
        for i in ans:
            print(i, end = " ")
        print("")
    return

if __name__ == "__main__":
    main()