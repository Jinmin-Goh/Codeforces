# Contest No.: 654
# Problem No.: E1
# Solver:      JEMINI
# Date:        20200701

import sys
import heapq

def main():
    n, p = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = []

    # check only min to max
    # maybe O(n ^ 3) for E1
    nums.sort()

    print(len(ans))
    if not ans:
        print("", end = "")
    else:
        ans.sort()
        for i in ans:
            print(i, end = " ")
    
    return

if __name__ == "__main__":
    main()