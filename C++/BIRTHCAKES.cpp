#include <bits/stdc++.h>
#define arrMAX 1000000
using namespace std;

int n, a[arrMAX];

void input () {
    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> a[i];
}

void solve () {
    input(); sort(a, a+n);
    int cnt = n, i = 1, m = n / 2;
    for (int j = m + 1; j <= n && i <= m; ++j) {
        if (a[j] >= a[i]) {
            cnt--; i++;
        }
    }
    cout << cnt;
}

int main() {
    //ios_base::sync_with_stdio(0);
    freopen("BIRTHCAKES.INP","r",stdin);
    freopen("BIRTHCAKES.OUT","w",stdout);
    solve();
    return 0;
}
