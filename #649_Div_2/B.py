# Contest No.: 649
# Problem No.: B
# Solver:      JEMINI
# Date:        20200613

import sys
import heapq

# must be O(n log n) or less

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        if n == 2:
            print(2)
            print(nums[0], nums[1])
            continue
        
        ans = []
        #ans.append(nums[0])
        diffFlag = False
        for i in range(n - 1):
            if nums[i + 1] != nums[i]:
                diffFlag = True
                break
        if not diffFlag:
            print(2)
            print(nums[0], nums[1])
            continue
        
        for pointer in range(2, n):
            #print(pointer, nums[pointer - 2:pointer + 1])

            # local maximum
            if nums[pointer - 2] < nums[pointer - 1] and nums[pointer] < nums[pointer - 1]:
                if pointer - 2 == 0:
                    ans.append(nums[pointer - 2])
                ans.append(nums[pointer - 1])    
                if pointer == n - 1:
                    ans.append(nums[pointer])
            # local minimuim
            elif nums[pointer - 2] > nums[pointer - 1] and nums[pointer] > nums[pointer - 1]:
                if pointer - 2 == 0:
                    ans.append(nums[pointer - 2])
                ans.append(nums[pointer - 1])    
                if pointer == n - 1:
                    ans.append(nums[pointer])
            # \_ shape
            elif nums[pointer - 2] > nums[pointer - 1] and nums[pointer] == nums[pointer - 1]:
                if pointer - 2 == 0:
                    ans.append(nums[pointer - 2])
                ans.append(nums[pointer - 1])
            #  _
            # / shape
            elif nums[pointer - 2] < nums[pointer - 1] and nums[pointer] == nums[pointer - 1]:
                if pointer - 2 == 0:
                    ans.append(nums[pointer - 2])
                ans.append(nums[pointer - 1])
            # _/ shape
            elif nums[pointer - 2] == nums[pointer - 1] and nums[pointer] > nums[pointer - 1]:
                ans.append(nums[pointer - 1])
                if pointer == n - 1:
                    ans.append(nums[pointer])
            #  _
            #   \shape
            elif nums[pointer - 2] == nums[pointer - 1] and nums[pointer] < nums[pointer - 1]:
                ans.append(nums[pointer - 1])
                if pointer == n - 1:
                    ans.append(nums[pointer])
            else:
                if pointer == 2 and nums[0] != nums[1]:
                    ans.append(nums[0])
                if pointer == n - 1 and nums[-1] != nums[-2]:
                    ans.append(nums[-1])
                
            #pointer += 1

        
        print(len(ans))
        for i in ans:
            print(i, end = " ")
        print("")

        #while pRear < n and pFront < n:
        #    if nums[pFront] == nums[pRear]:
        #        if decFlag:
#
        #        elif incFlag:
#
        #        else:
        #        pFront += 1
        #        pRear += 1
        #    elif nums[pFront] > nums[pRear]:
        #        # was decreasing
        #        if decFlag:
        #            pRear += 1
        #        # was increasing
        #        elif incFlag:
        #            incFlag = False
        #            decFlag = True
        #            ans.append(nums[pFront])
        #            pFront = pRear - 1
        #        # was flat
        #        else:
        #            decFlag = True
#
        #    else:
#
        
        
    return

if __name__ == "__main__":
    main()