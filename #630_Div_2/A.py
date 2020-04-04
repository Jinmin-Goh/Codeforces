# Problem No.: A
# Solver:      Jinmin Goh
# Date:        20200331

import sys

def main():
    n = int(input())
    for _ in range(n):
        a, b, c, d = map(int, sys.stdin.readline().split())
        x, y, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        if not (x1 <= x <= x2) or not (y1 <= y <= y2):
            print("No")
            continue
        if x1 == x2 and (a or b):
            print("No")
            continue
        if y1 == y2 and (c or d):
            print("No")
            continue
        xMove = b - a
        yMove = d - c
        if (xMove > 0 and x2 - x < xMove) or (xMove < 0 and x - x1 < -xMove):
            print("No")
            continue
        if (yMove > 0 and y2 - y < yMove) or (yMove < 0 and y - y1 < -yMove):
            print("No")
            continue
        print("Yes")
    return

if __name__ == "__main__":
    main()