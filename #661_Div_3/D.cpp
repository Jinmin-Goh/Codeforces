// Contest No.: 661
// Problem No.: D
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

char nums[200010];
int belong[200010];
set<int> stringSet[2];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        scanf("%s", nums);
        int remain = n, cnt = 1;
        for(int i = 0; i < n; i++) {
            belong[i] = 1;
        }
        stringSet[0].clear();
        stringSet[1].clear();

        for(int i = 0; i < n; i++) {
            int k = nums[i] - '0';
            if(stringSet[k].empty()) {
                belong[i] = cnt;
                stringSet[1 - k].insert(cnt);
                cnt++;
            }
            else {
                int temp = *(stringSet[k].begin());
                belong[i] = temp;
                stringSet[k].erase(temp);
                stringSet[1 - k].insert(temp);
            }
        }
        printf("%d\n", cnt - 1);
        for(int i = 0; i < n; i++) {
            printf("%d ", belong[i]);
        }
        printf("\n");
    }
    return 0;
}