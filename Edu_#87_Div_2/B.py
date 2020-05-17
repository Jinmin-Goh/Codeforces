# Contest No.: Edu 87
# Problem No.: B
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        pos1 = None
        pos2 = None
        pos3 = None
        ans = len(s)
        for i in range(len(s)):
            if s[i] == "1":
                pos1 = i
            elif s[i] == "2":
                pos2 = i
            else:
                pos3 = i
            if not(pos1 == None or pos2 == None or pos3 == None):
                ans = min(ans, max(pos1, pos2, pos3) - min(pos1, pos2, pos3) + 1)
        if pos1 == None or pos2 == None or pos3 == None:
            print(0)
        else:
            print(ans)
    return

if __name__ == "__main__":
    main()