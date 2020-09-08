// Contest No.: 669
// Problem No.: C
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

int ans[10010];

int main() {
    int n;
    scanf("%d", &n);
    int u = 1;
    for(int i = 2; i <= n; i++){
        int umi, imu;
        printf("? %d %d\n", u, i);
        fflush(stdout);
        scanf("%d", &umi);
        printf("? %d %d\n", i, u);
        fflush(stdout);
        scanf("%d", &imu);
        if(umi > imu){
            ans[u] = umi;
            u = i;
        }
        else{
            ans[i] = imu;
        }
    }
    ans[u] = n;
    printf("! ");
    for(int i = 1; i <= n; i++) {
        printf("%d ", ans[i]);
    }
    printf("\n");
    fflush(stdout);

    return 0;
}