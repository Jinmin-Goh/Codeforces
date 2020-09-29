// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200928

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

int nums[300010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t ; _++) {
        int n, m;
        scanf("%d %d", &n, &m);
        bool flag = false;
        for(int i = 0; i < n; i++ ) {
            int a, b, c, d;
            scanf("%d %d\n%d %d", &a, &b, &c, &d);
            if(b == c) {
                flag = true;
            }
        }
        if(m % 2) {
            printf("NO\n");
            continue;
        }
        if(flag) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }



    }
    return 0;
}