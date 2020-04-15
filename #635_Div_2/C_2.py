# Contest No.: 635
# Problem No.: C
# Solver:      JEMINI
# Date:        20200416
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
    n, k = map(int, input().split())
    graph = {}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    
    industrySet = set()
    ans = 0
    flag = True
    costList = []
    while k > 0:
        if flag:
            visited = set([1])
            temp = [1]
            cnt = 1
            costList = []
            while temp:
                nextList = []
                for i in temp:
                    visited.add(i)
                    for j in graph[i]:
                        if j not in visited:
                            nextList.append(j)
                    if i not in industrySet:
                        costList.append([cnt - 1 - (len(graph[i]) - 1), i])
                if i not in industrySet:
                    cnt += 1
                temp = nextList[:]
            costList.sort()
        ans += costList[-1][0]
        industrySet.add(costList[-1][1])
        check = 0
        checkFlag = False
        for i in graph[costList[-1][1]]:
            if i not in industrySet:
                check += 1
            if i in graph[i]:
                checkFlag = True
        if check > 1 or costList[-1][1] == 1 or checkFlag:
            flag = True
        else:
            flag = False
            costList.pop()
        k -= 1
    print(ans)
    return

if __name__ == "__main__":
    main()