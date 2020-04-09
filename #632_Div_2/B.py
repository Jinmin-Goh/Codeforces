# Contest No.: 632
# Problem No.: B
# Solver:      JEMINI
# Date:        20200408

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline())
        list1 = list(map(int, sys.stdin.readline().split()))
        list2 = list(map(int, sys.stdin.readline().split()))
        list1Dict = {-1:0, 0:0, 1:0}
        flag = True
        for i in range(n):
            if list1[i] == list2[i]:
                pass
            elif list1[i] < list2[i]:
                if list1Dict[1]:
                    pass
                else:
                    flag = False
                    break
            elif list1[i] > list2[i]:
                if list1Dict[-1]:
                    pass
                else:
                    flag = False
                    break
            list1Dict[list1[i]] += 1
        if flag:
            print("YES")
        else:
            print("NO")
    return

if __name__ == "__main__":
    main()