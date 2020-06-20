# Contest No.: 651
# Problem No.: D
# Solver:      JEMINI
# Date:        20200620

import sys
import heapq

def main():
    n, k = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().split()))
    evenMaxHeap = []
    evenMinVal = max(nums)
    oddMaxHeap = []
    oddMinVal = max(nums)
    for i in range(k):
        if nums[i] % 2:
            oddMaxHeap.append([-nums[i], i])
            oddMinVal = min(oddMinVal, nums[i])
        else:
            evenMaxHeap.append([-nums[i], i])
            evenMinVal = min(evenMinVal, nums[i])
    heapq.heapify(evenMaxHeap)
    heapq.heapify(oddMaxHeap)
    
    #print(evenMaxHeap)
    #print(oddMaxHeap)


    for i in range(k, n):
        if nums[i] % 2:
            if not evenMaxHeap:
                if nums[i] < -oddMaxHeap[0][0]:
                    heapq.heappop(oddMaxHeap)
                    heapq.heappush(oddMaxHeap, [-nums[i], i])
                    oddMinVal = min(oddMinVal, nums[i])

            elif not oddMaxHeap:
                if nums[i] < -evenMaxHeap[0][0]:
                    heapq.heappop(evenMaxHeap)
                    heapq.heappush(oddMaxHeap, [-nums[i], i])
                    oddMinVal = min(oddMinVal, nums[i])

            elif nums[i] < max(-oddMaxHeap[0][0], -evenMaxHeap[0][0]):
                tempEven = heapq.heappop(evenMaxHeap)
                tempOdd = heapq.heappop(oddMaxHeap)

                if evenMaxHeap and oddMaxHeap:
                    if nums[i] < -tempOdd[0] and max(nums[i], -oddMaxHeap[0][0]) < -tempEven[0]:
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    elif max(nums[i], -tempOdd[0]) > -evenMaxHeap[0][0]:
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    else:
                        heapq.heappush(oddMaxHeap, tempOdd)
                        heapq.heappush(evenMaxHeap, tempEven)

                elif not evenMaxHeap:
                    if -tempEven[0] > min(oddMinVal, nums[i]):
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    else:
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)

                elif not oddMaxHeap:
                    if -evenMaxHeap[0][0] > max(nums[i], -tempOdd[0]):
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    elif -tempOdd[0] > nums[i]:
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    else:
                        heapq.heappush(oddMaxHeap, tempOdd)
                        heapq.heappush(evenMaxHeap, tempEven)

                else:
                    if -tempOdd[0] > nums[i]:
                        heapq.heappush(oddMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    else:
                        heapq.heappush(oddMaxHeap, tempOdd)
                        heapq.heappush(evenMaxHeap, tempEven)

        else:
            if not oddMaxHeap:
                if nums[i] < -evenMaxHeap[0][0]:
                    heapq.heappop(evenMaxHeap)
                    heapq.heappush(evenMaxHeap, [-nums[i], i])
                    evenMinVal = min(evenMinVal, nums[i])

            elif not evenMaxHeap:
                if nums[i] < -oddMaxHeap[0][0]:
                    heapq.heappop(oddMaxHeap)
                    heapq.heappush(evenMaxHeap, [-nums[i], i])
                    evenMinVal = min(evenMinVal, nums[i])

            elif nums[i] < max(-evenMaxHeap[0][0], -oddMaxHeap[0][0]):
                tempOdd = heapq.heappop(oddMaxHeap)
                tempEven = heapq.heappop(evenMaxHeap)

                if oddMaxHeap and evenMaxHeap:
                    if nums[i] < -tempEven[0] and max(nums[i], -evenMaxHeap[0][0]) < -tempOdd[0]:
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    elif max(nums[i], -tempEven[0]) > -oddMaxHeap[0][0]:
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    else:
                        heapq.heappush(evenMaxHeap, tempEven)
                        heapq.heappush(oddMaxHeap, tempOdd)

                elif not oddMaxHeap:
                    if -tempOdd[0] > min(evenMinVal, nums[i]):
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    else:
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)

                elif not evenMaxHeap:
                    if -oddMaxHeap[0][0] > max(nums[i], -tempEven[0]):
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(evenMaxHeap, tempEven)
                    elif -tempEven[0] > nums[i]:
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    else:
                        heapq.heappush(evenMaxHeap, tempEven)
                        heapq.heappush(oddMaxHeap, tempOdd)

                else:
                    if -tempEven[0] > nums[i]:
                        heapq.heappush(evenMaxHeap, [-nums[i], i])
                        heapq.heappush(oddMaxHeap, tempOdd)
                    else:
                        heapq.heappush(evenMaxHeap, tempEven)
                        heapq.heappush(oddMaxHeap, tempOdd)

        print(evenMaxHeap)
        print(oddMaxHeap)

    if oddMaxHeap and evenMaxHeap:
        print(min(-oddMaxHeap[0][0], -evenMaxHeap[0][0]))
    elif not oddMaxHeap:
        print(evenMinVal)
    elif not evenMaxHeap:
        print(oddMinVal)

    return

if __name__ == "__main__":
    main()