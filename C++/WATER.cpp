#include <bits/stdc++.h>
using namespace std;
int n, k, a;

void solve () {
    cin >> n >> k; int m = k;
    for (int i = 1; i <= n; ++i) {
        cin >> a;
        if (k % a == 0) m = min(m, k / a);
    }
    cout << m;
}

int main () {
    freopen ("WATER.INP", "r", stdin);
    freopen ("WATER.OUT", "w", stdout);
    solve();
    return 0;
}
