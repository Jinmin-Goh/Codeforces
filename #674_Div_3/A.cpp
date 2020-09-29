// Problem No.: A
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
        int n, x;
        scanf("%d %d", &n, &x);
        if(n <= 2) {
            printf("1\n");
            continue;
        }
        else {
            printf("%d\n", (n - 2 + x - 1) / x + 1);
        }
    }
    return 0;
}