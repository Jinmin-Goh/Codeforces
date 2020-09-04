// Contest No.: 667
// Problem No.: C
// Solver:      Jinmin Goh
// Date:        20200904

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
        int n, x, y;
        scanf("%d %d %d", &n, &x, &y);
        int refN = n;
        while((y - x) % (n - 1)) {
            n--;
        }
        int diff = (y - x) / (n - 1);
        int cnt = 0;
        for(int i = x; i <= y; i += diff) {
            printf("%d ", i);
            cnt++;
        }
        if(cnt < refN) {
            for(int i = x - diff; i > 0; i -= diff) {
                printf("%d ", i);
                cnt++;
                if(cnt >= refN) {
                    break;
                }
            }
        }
        if(cnt < refN) {
            for(int i = y + diff; cnt < refN; i += diff) {
                printf("%d ", i);
                cnt++;
                if(cnt >= refN) {
                    break;
                }
            }
        }
        printf("\n");
    }
    return 0;
}