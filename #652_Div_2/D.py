# Contest No.: 652
# Problem No.: D
# Solver:      JEMINI
# Date:        20200623

import sys
import heapq

def main():
    modVal = 10 ** 9 + 7

    ans = [0] * ((2 * (10 ** 6)) + 1)
    ans[3] = 4
    ans[4] = 4
    ans[5] = 12
    for i in range(6, (2 * (10 ** 6)) + 1):
        ans[i] = ans[i - 1] + 2 * ans[i - 2]
        if i % 3 == 0:
            ans[i] += 4
        ans[i] = ans[i] % modVal
    
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        print(ans[n])

    return

if __name__ == "__main__":
    main()