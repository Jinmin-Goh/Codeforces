// Contest No.: 664
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200812

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int n, m, Sx, Sy, nums[200010];

int main() {
    scanf("%d %d %d %d", &n, &m, &Sx, &Sy);
    bool rightFlag = true;
    //printf("%d %d\n", Sx, Sy);
    if(Sy == 1) {
        rightFlag = false;
        for(int i = 1; i <= m; i++) {
            printf("%d %d\n", Sx, i);
        }
    }
    else {
        for(int i = Sy; i <= m; i++) {
            printf("%d %d\n", Sx, i);
        }
        for(int i = Sy - 1; i > 0; i--) {
            printf("%d %d\n", Sx, i);
        }
    }

    for(int i = 1; i <= n; i++) {
        if(i == Sx) {
            continue;
        }
        if(rightFlag)
        {
            for(int j = 1; j <= m; j++) {
                printf("%d %d\n", i, j);
            }
        }
        else {
            for(int j = m; j > 0; j--) {
                printf("%d %d\n", i, j);
            }
        }
        rightFlag = !rightFlag;
    }
    return 0;
}