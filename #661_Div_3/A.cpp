// Contest No.: 661
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200805

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

int nums[100000];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
        }
        sort(nums, nums + n);
        bool flag = false;
        for(int i = 1; i < n; i++) {
            if(abs(nums[i] - nums[i - 1]) > 1) {
                flag = true;
            }
        }
        if(flag) {
            printf("NO\n");
        }
        else {
            printf("YES\n");
        }
    }
    return 0;
}