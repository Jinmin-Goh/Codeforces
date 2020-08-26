// Contest No.: Edu94
// Problem No.: C
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

char nums[100010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int x;
        scanf("%s", nums);
        scanf("%d", &x);

        char ans[100010], newList[100010];
        int n = 0;
        for(int i = 0; nums[i] != NULL; i++) {
            ans[i] = '1';
            newList[i] = '0';
            n++;
        }
        for(int i = 0; i < n; i++) {
            if(nums[i] == '0') {
                if(i >= x) {
                    ans[i - x] = '0';
                }
                if(i + x < n) {
                    ans[i + x] = '0';
                }
            }
        }
        bool flag = false;
        
        
        for(int i = 0; i < n - x; i++) {
            if(ans[i] == '1') {
                newList[i + x] = '1';
            }
        }
        for(int i = x; i < n; i++) {
            if(ans[i] == '1') {
                newList[i - x] = '1';
            }
        }

        for(int i = 0; i < n; i++) {
            if(nums[i] != newList[i]) {
                flag = true;
                break;
            }
        }

        if(!flag) {
            for(int i = 0; i < n; i++) {
                printf("%c", ans[i]);
            }
        }
        else {
            printf("-1");
        }
        printf("\n");
    }
    return 0;
}