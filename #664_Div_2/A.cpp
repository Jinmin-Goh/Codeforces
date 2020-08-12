// Contest No.: 664
// Problem No.: A
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

int r, g, b, w, nums[200010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        scanf("%d %d %d %d", &r, &g, &b, &w);
        int oddCnt = 0;
        if(r % 2) {
            oddCnt++;
        }
        if(g % 2) {
            oddCnt++;
        }
        if(b % 2) {
            oddCnt++;
        }
        if(((oddCnt == 1) && !(w % 2)) || ((oddCnt == 0))) {
            printf("Yes\n");
        }
        else if((((r % 2 && r > 0 && g % 2 && g > 0 && b > 0) || (r % 2 && r > 0 && b % 2 && b > 0 && g > 0) || (b % 2 && b > 0 && g % 2 && g > 0 && r > 0)) && w % 2) || (oddCnt == 3 && r > 0 && g > 0 && b > 0)) {
            printf("Yes\n");
        }
        else {
            printf("No\n");
        }

    }
    return 0;
}