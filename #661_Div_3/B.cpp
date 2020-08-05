// Contest No.: 661
// Problem No.: B
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

int A[100000];
int B[100000];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n, minA = 1e9, minB = 1e9;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &A[i]);
            minA = min(minA, A[i]);
        }
        for(int i = 0; i < n; i++) {
            scanf("%d", &B[i]);
            minB = min(minB, B[i]);
        }
        long long int ans = 0;
        for(int i = 0; i < n; i++) {
            ans += max(A[i] - minA, B[i] - minB);
        }
        printf("%lld\n", ans);
        
    }
    return 0;
}