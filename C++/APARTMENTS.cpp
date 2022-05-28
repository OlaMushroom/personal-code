#include <bits/stdc++.h>
#define arrMAX 200000
using namespace std;

int n, m, k, b[arrMAX];
struct s {
    int mx, mn;
} a[arrMAX];

void input () {
    cin >> n >> m >> k;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].mx;
        a[i].mn = a[i].mx - k;
        a[i].mx += k;
    }
    for (int i = 0; i < m; ++i) cin >> b[i];
}

bool cmp (s x, s y) {
    return (x.mx < y.mx);
}

void solve () {
    input(); sort(a, a+n, cmp); sort (b, b+m);
    int cnt = 0, i = 0, j = 0;
    while (i < n && j < m) {
        if (a[i].mx >= b[j] && a[i].mn <= b[j]) {
            cnt++; i++; j++;
        }
        if (a[i].mx < b[j]) i++;
        if (a[i].mn > b[j]) j++;
    }
    cout << cnt;
}

int main()
{
    //ios_base::sync_with_stdio(0);
    freopen("APARTMENTS.INP","r",stdin);
    freopen("APARTMENTS.OUT","w",stdout);
    solve();
    return 0;
}
