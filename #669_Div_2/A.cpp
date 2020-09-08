// Contest No.: 669
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200908

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
        int cnt1 = 0;
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
            if(nums[i]) cnt1++;
        }
        
        if(cnt1 <= n / 2) {
            printf("%d\n", n / 2);
            for(int i = 0; i < n / 2; i++) {
                printf("0 ");
            }
            printf("\n");
        }
        else {
            if(n % 4) {
                printf("%d\n", n / 2 + 1);
            }
            else
                printf("%d\n", n / 2);
            for(int i = 0; i < n / 2; i++) {
                printf("1 ");
            }
            if(n % 4) {
                printf("1 ");
            }
            printf("\n");
        }
    }
    return 0;
}