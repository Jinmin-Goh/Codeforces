# Contest No.: Edu91
# Problem No.: A
# Solver:      JEMINI
# Date:        20200712

# UNRATED CONTEST

import sys
import heapq
import collections

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        ans = None
        for i in range(n - 2):
            if nums[i] < nums[i + 1] and nums[i + 1] > nums[i + 2]:
                ans = [i + 1, i + 2, i + 3]
        if ans:
            print("YES")
            for i in ans:
                print(i, end = " ")
            print("")
        else:
            print("NO")
    return

if __name__ == "__main__":
    main()