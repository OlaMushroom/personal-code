#include <bits/stdc++.h>
#define arrMAX 100000
using namespace std;

int n, a[arrMAX];

void solve ()
{
    cin >> n; for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a+n); a[n] = a[n-1] + 1;
    int v = 0, f = 0, maxf = 0;
    for (int i = 0; i < n; ++i) {
        ++f;
        if (a[i] != a[i + 1]) {
            if (f > maxf) {
                v = a[i]; maxf = f;
            }
            f = 0;
        }
    }
    cout << v;
}

int main() {
    freopen("MAXFREQ.INP","r",stdin);
    freopen("MAXFREQ.OUT","w",stdout);
    solve();
    return 0;
}
