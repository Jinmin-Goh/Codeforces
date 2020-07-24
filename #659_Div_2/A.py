# Contest No.: 659
# Problem No.: A
# Solver:      JEMINI
# Date:        20200724

import sys
import heapq

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        init = "a" * 100
        print(init)
        for i in range(n):
            temp = init[:nums[i]]
            if init[nums[i]] == "a":
                temp += "b"
            else:
                temp += "a"
            temp += "a" * (110 - len(temp))
            print(temp)
            init = temp

        
    return

if __name__ == "__main__":
    main()