# Contest No.: 645
# Problem No.: C
# Solver:      JEMINI
# Date:        20200526

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
        if x1 == x2 or y1 == y2:
            print(1)
            continue
        xDiff = x2 - x1
        yDiff = y2 - y1
        if xDiff == 1:
            print(y2 - y1 + 1)
            continue
        if yDiff == 1:
            print(x2 - x1 + 1)
            continue
        upRight = (x1 + y1 - 1) * xDiff + xDiff * (xDiff - 1) // 2
        downLeft = (x1 + y1) * yDiff + yDiff * (yDiff - 1) // 2
        #print(upRight, downLeft)
        minVal = xDiff * (xDiff + 1) * (x1 + y1 - 1) // 2 + (xDiff * (xDiff + 1) * (2 * xDiff + 1) // 6 - xDiff * (xDiff + 1) // 2) // 2 + yDiff * upRight + yDiff * (yDiff + 1) * (x2 + y1) // 2 + (yDiff * (yDiff + 1) * (2 * yDiff + 1) // 6 - yDiff * (yDiff + 1) // 2) // 2
        maxVal = yDiff * (yDiff + 1) * (x1 + y1) // 2 + (yDiff * (yDiff + 1) * (2 * yDiff + 1) // 6 - yDiff * (yDiff + 1) // 2) // 2 + xDiff * downLeft + xDiff * (xDiff + 1) * (x1 + y2 - 1) // 2 + (xDiff * (xDiff + 1) * (2 * xDiff + 1) // 6 - xDiff * (xDiff + 1) // 2) // 2
        #print(minVal, maxVal)
        print(maxVal - minVal + 1)
    return

if __name__ == "__main__":
    main()