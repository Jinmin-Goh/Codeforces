# Contest No.: Edu 85
# Problem No.: C
# Solver:      JEMINI
# Date:        20200410

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

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        health = []
        damage = []
        
        delSum = 0
        #temp = [None]
        tempMin = 10 ** 12
        minHealth = 10 ** 12
        tempH = None
        zeroH = None
        tempD = None
        zeroD = None
        for i in range(n):
            h, d = map(int, input().split())
            health.append(h)
            damage.append(d)
            minHealth = min(minHealth, h)
            if i == 0:
                zeroH = h
                zeroD = d
            if i != 0:
                #temp.append(max(0, h - tempD))
                delSum += max(0, h - tempD)
                tempMin = min(tempMin, h - max(0, h - tempD))
            if i == n - 1:
                #temp.append(max(0, health[0] - damage[i]))
                delSum += max(0, zeroH - d)
                tempMin = min(tempMin, zeroH - max(0, zeroH - d))
            tempH = h
            tempD = d
        
        # case 1 - all satisfied and kill min health
        if delSum == 0:
            print(minHealth)
            continue
        #print(temp, delSum)
        
        # case 2 - make only one is not satisfied
        minVal = delSum + tempMin
        print(minVal)
    return

if __name__ == "__main__":
    main()