# Contest No.: 637
# Problem No.: B
# Solver:      JEMINI
# Date:        20200423

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        #peakList = []
        peakCheck = [False] * n
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                #peakList.append(i)
                peakCheck[i] = True
        #print(peakCheck)
        maxVal = sum(peakCheck[1:k - 1])
        ans = 0
        #print(maxVal)
        temp = maxVal
        for i in range(k, n):
            if peakCheck[i - k + 1]:
                temp -= 1
            if peakCheck[i - 1]:
                temp += 1
            if maxVal < temp:
                ans = i - k + 1
                maxVal = temp
        print(maxVal + 1, ans + 1)


    return

if __name__ == "__main__":
    main()