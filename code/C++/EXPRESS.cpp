#include <bits/stdc++.h>
#define arrMAX 100000
using namespace std;

int n, k, a[arrMAX];

void input () {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) cin >> a[i];
}

bool cmp (int x, int y) {
    return (x > y);
}

void solve () {
    input(); sort(a+1, a+n, cmp);
    long long s = a[0]; int i = 1;
    for (; i <= k; ++i) s += a[i];
    for (; i < n; ++i) s -= a[i];
    cout << s;
}

int main() {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("EXPRESS.INP","r",stdin);
    freopen("EXPRESS.OUT","w",stdout);
    solve();
    return 0;
}
