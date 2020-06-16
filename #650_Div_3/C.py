# Contest No.: 650
# Problem No.: C
# Solver:      JEMINI
# Date:        20200616

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        if len(s) == 1:
            if s[0] == "0":
                print(1)
            else:
                print(0)
            continue

        if n == k:
            if "1" in s:
                print(0)
            else:
                print(1)
            continue
        
        onePos = []
        nums = []
        for i in range(n):
            if s[i] == "1":
                onePos.append(i)
            nums.append(int(s[i]))
        
        if not onePos:
            ans = n // (k + 1)
            if n % (k + 1):
                ans += 1
            print(ans)
            continue
        
        invalid = []
        for pos in onePos:
            if not invalid:
                invalid.append([max(0, pos - k), min(n - 1, pos + k)])
                continue
            if pos - k <= invalid[-1][1]:
                invalid[-1][1] = min(n - 1, pos + k)
            else:
                invalid.append([max(0, pos - k), min(n - 1, pos + k)])
        #print(invalid)
        ans = 0
        pos = 0
        for i in invalid:
            ans += (i[0] - pos) // (k + 1)
            if (i[0] - pos) % (k + 1):
                ans += 1
            pos = i[1] + 1
        ans += (n - pos) // (k + 1)
        if (n - pos) % (k + 1):
            ans += 1
        print(ans)
        
    return

if __name__ == "__main__":
    main()