# Contest No.: 639
# Problem No.: D
# Solver:      JEMINI
# Date:        20200507

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

def main():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        temp = input()
        #temp2 = [_ for _ in temp]
        grid.append(temp)

    ansFlag = True
    wrow = 0
    wcol = 0
    # row check
    for i in range(n):
        invCnt = 0
        flag = True
        for j in range(m):
            if j > 0:
                if grid[i][j] != grid[i][j - 1]:
                    invCnt += 1
                if (invCnt == 2 and grid[i][0] == "#") or invCnt >= 3:
                    ansFlag = False
            if grid[i][j] == "#":
                flag = False
        if flag:
            wrow += 1   
    if not ansFlag:
        print(-1)
        return

    # col check
    for j in range(m):
        invCnt = 0
        flag = True
        for i in range(n):
            if i > 0:
                if grid[i][j] != grid[i - 1][j]:
                    invCnt += 1
                if (invCnt == 2 and grid[0][j] == "#") or invCnt >= 3:
                    ansFlag = False
            if grid[i][j] == "#":
                flag = False
        if flag:
            wcol += 1
    if not ansFlag:
        print(-1)
        return

    if wcol * wrow == 0 and wcol + wrow > 0:
        print(-1)
        return
    visitedSet = set()
    # count connected elements -> min of N        
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" and (i, j) not in visitedSet:
                #BFS
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    visitedSet.add((x, y))
                    # make visited
                    #grid[x][y] = "*"
                    if x > 0 and (x - 1, y) not in visitedSet and grid[x - 1][y] == "#":
                        stack.append((x - 1, y))
                    if x < n - 1 and (x + 1, y) not in visitedSet and grid[x + 1][y] == "#":
                        stack.append((x + 1, y))
                    if y > 0 and (x, y - 1) not in visitedSet and grid[x][y - 1] == "#":
                        stack.append((x, y - 1))
                    if y < m - 1 and (x, y + 1) not in visitedSet and grid[x][y + 1] == "#":
                        stack.append((x, y + 1))
                ans += 1
    print(ans)
        

    return

if __name__ == "__main__":
    main()