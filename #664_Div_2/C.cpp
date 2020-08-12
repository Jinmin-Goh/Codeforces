// Contest No.: 664
// Problem No.: C
// Solver:      Jinmin Goh
// Date:        20200812

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

int n, m, nList[210], mList[210], checkTable[210][210];

int main() {
    
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nList[i]);
    }
    for(int i = 0; i < m; i++) {
        scanf("%d", &mList[i]);
    }
    int ans = 0;
    for(int k = 9; k >= 0; k--) {
        int C = 0;
        for(int i = 0; i < n; i++) {
            int D = 4095;
            for(int j = 0; j < m; j++) {
                if(checkTable[i][j] == 1) {
                    continue;
                }
                D &= (nList[i] & mList[j]);
            }
            C |= D;
        }
        if((C & (1 << k)) != 0) {
			ans += (1 << k);
		}
		else {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					if(checkTable[i][j] == 1) {
                        continue;
                    }
					if(((nList[i] & mList[j]) & (1 << k)) != 0) checkTable[i][j] = 1;
				}
			}
		}
    }

    printf("%d", ans);

    return 0;
}