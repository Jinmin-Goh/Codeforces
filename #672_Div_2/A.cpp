// Contest No.: 672
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200924

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

int nums[200010], sortedNums[200010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
            sortedNums[i] = nums[i];
        }
        sort(sortedNums, sortedNums + n);

        int cnt = 0;
        for(int i = 0; i < n; i++) {
            if(sortedNums[i] != nums[i]) {
                break;
            }
            cnt++;
        }
        if(cnt == n) {
            printf("YES\n");
            continue;
        }
        cnt == 0;
        for(int i = 0; i < n - 1; i++) {
            if(nums[i + 1] >= nums[i]) {
                break;
            }
            cnt++;
        }
        if(cnt == n - 1) {
            printf("NO\n");
        }
        else {
            printf("YES\n");
        }

    }
    return 0;
}