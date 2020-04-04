# Problem No.: B
# Solver:      Jinmin Goh
# Date:        20200403
 
import sys
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        # ans is always one of 2, 1, 0
        leftSet = set()
        rightSet = set()
        ans = []
        flag = True
        validFlag = True
        for i in range(len(nums)):
            if flag:
                if nums[i] in leftSet:
                    flag = False
                    if max(leftSet) != len(leftSet):
                        validFlag = False
                        break
                else:
                    leftSet.add(nums[i])
            if not flag:
                if nums[i] in rightSet:
                    validFlag = False
                    break
                else:
                    rightSet.add(nums[i])
        if validFlag:
            if leftSet and rightSet and max(leftSet) == len(leftSet) and max(rightSet) == len(rightSet):
                ans.append([len(leftSet), len(rightSet)])
        flag = True
        validFlag = True
        leftSet = set()
        rightSet = set()
        for i in reversed(range(len(nums))):
            if flag:
                if nums[i] in rightSet:
                    flag = False
                    if max(rightSet) != len(rightSet):
                        validFlag = False
                        break
                else:
                    rightSet.add(nums[i])
            if not flag:
                if nums[i] in leftSet:
                    validFlag = False
                    break
                else:
                    leftSet.add(nums[i])
        if validFlag:
            if leftSet and rightSet and max(leftSet) == len(leftSet) and max(rightSet) == len(rightSet):
                if [len(leftSet), len(rightSet)] not in ans:
                    ans.append([len(leftSet), len(rightSet)])
        print(len(ans))
        for i in ans:
            print(i[0], i[1])
    return
 
if __name__ == "__main__":
    main()