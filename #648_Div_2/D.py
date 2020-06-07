# Contest No.: 648
# Problem No.: D
# Solver:      JEMINI
# Date:        20200607

##### FAST INPUT #####
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
##### END OF FAST INPUT #####

#import sys
import heapq
import collections

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        table = []
        BList = []
        GList = []
        for i in range(n):
            temp = input().strip()
            table.append([])
            for j in range(m):
                table[-1].append(temp[j])
                if table[-1][-1] == "B":
                    BList.append((i, j))
                if table[-1][-1] == "G":
                    GList.append((i, j))
        if not GList:
            print("Yes")
            continue
        flag = True
        #print(BList, GList)
        if BList:
            BList = collections.deque(BList)
            while BList:
                BList.append(None)
                while True:
                    temp = BList.popleft()
                    if temp == None:
                        break
                    x, y = temp[0], temp[1]
                    #print(table[x][y])
                    if table[x][y] == "B":
                        table[x][y] = "."
                        if x > 0:
                            BList.append((x - 1, y))
                        if x < n - 1:
                            BList.append((x + 1, y))
                        if y > 0:
                            BList.append((x, y - 1))
                        if y < m - 1:
                            BList.append((x, y + 1))
                    if table[x][y] == ".":
                        table[x][y] = "#"
                    if table[x][y] == "G":
                        flag = False
                        break
                #print(BList)
                if not flag:
                    break
        #print(table)
        if not flag or table[-1][-1] == "#":
            print("No")
            continue
        
        cnt = 0
        stack = [(n - 1, m - 1)]
        while stack:
            x, y = stack.pop()
            if table[x][y] in ["*", "#"]:
                continue
            if table[x][y] in [".", "G"]:
                if table[x][y] == "G":
                    cnt += 1
                if x > 0:
                    stack.append((x - 1, y))
                if x < n - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < m - 1:
                    stack.append((x, y + 1))    
            table[x][y] = "*"
        if cnt == len(GList):
            print("Yes")
        else:
            print("No")
            
        
    return

if __name__ == "__main__":
    main()