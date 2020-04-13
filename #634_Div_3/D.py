# Contest No.: 634
# Problem No.: D
# Solver:      JEMINI
# Date:        20200414

import sys

def search(depth: int, table: [[int]], usedRow: [int], usedCol: [int], usedBox: [int], ans: [int]) -> bool:
    if len(ans) == 9:
        return True
    #print(ans)
    flag = False
    for i in range(9):
        if i in usedCol:
            continue
        if 3 * (depth // 3) + i // 3 in usedBox:
            continue
        #print(depth, i)
        newUsedRow = usedRow[:]
        newUsedRow.append(depth)
        newUsedCol = usedCol[:]
        newUsedCol.append(i)
        newUsedBox = usedBox[:]
        newUsedBox.append(3 * (depth // 3) + i // 3)
        ans.append([depth, i])
        flag = search(depth + 1, table, newUsedRow, newUsedCol, newUsedBox, ans)
        if flag:
            break
        ans.pop()
    return flag
        

def main():
    t = int(input())
    for _ in range(t):
        table = []
        for i in range(9):
            temp = sys.stdin.readline().strip()
            table.append([])
            for j in temp:
                table[-1].append(j)
        for i in range(9):
            ans = [[0, i]]
            flag = search(1, table, [0], [i], [i // 3], ans)
            if flag:
                break
        for i in ans:
            table[i[0]][i[1]] = int(table[i[0]][i[1]]) + 1
            if table[i[0]][i[1]] == 10:
                table[i[0]][i[1]] = 1
        for i in table:
            temp = ""
            for j in i:
                temp += str(j)
            print(temp)
    return

if __name__ == "__main__":
    main()