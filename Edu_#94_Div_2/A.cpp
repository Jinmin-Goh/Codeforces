// Contest No.: Edu94
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200825

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
        char nums[110];
        scanf("%d", &n);
        scanf("%s", nums);

        for(int i = 0; i < n; i++)
            printf("%c", nums[n - 1]);
        printf("\n");
    }
    return 0;
}