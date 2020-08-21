// Contest No.: 665
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200821

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

int nums[200010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int ans, x1, y1, z1, x2, y2, z2;
        scanf("%d %d %d", &x2, &y2, &z2);
        scanf("%d %d %d", &x1, &y1, &z1);
        ans = 0;
        int minVal = min(z2, y1);
        ans += 2 * minVal;
        z2 -= minVal;
        y1 -= minVal;

        minVal = min(x2, z1);
        x2 -= minVal;
        z1 -= minVal;

        minVal = min(y2, x1);
        y2 -= minVal;
        x1 -= minVal;

        if(z1 * y2 == 0) {
            printf("%d\n", ans);
            continue;
        }
        
        minVal = min(z1, z2);
        z1 -= minVal;
        z2 -= minVal;

        minVal = min(y1, y2);
        y1 -= minVal;
        y2 -= minVal;

        ans -= 2 * min(z1, y2);

        printf("%d\n", ans);

    }
    return 0;
}