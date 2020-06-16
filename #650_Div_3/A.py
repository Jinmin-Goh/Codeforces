# Contest No.: 650
# Problem No.: A
# Solver:      JEMINI
# Date:        20200616

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        ans = s[0]
        for i in range(len(s) // 2):
            ans += s[2 * i + 1]
        print(ans)
    return

if __name__ == "__main__":
    main()