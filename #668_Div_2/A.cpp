// Contest No.: 668
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200906

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
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
        }
        for(int i = n - 1; i >= 0; i--) {
            printf("%d ", nums[i]);
        }
        printf("\n");
    }
    return 0;
}