#include <bits/stdc++.h>
#define arrMAX 100000
using namespace std;

int n; long long c;
struct s {
    int a, b;
} arr[arrMAX];

void input () {
    cin >> n >> c;
    for (int i = 0; i < n; ++i) cin >> arr[i].a >> arr[i].b;
}

bool cmp (s x, s y) {
    if (x.a == y.a) return (x.b >= y.b);
    return (x.a < y.a);
}

void solve () {
    input();
    sort(arr, arr+n, cmp);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (c >= arr[i].a) {
            cnt++;
            c += arr[i].b;
        }
    }
    cout << cnt;
}

int main() {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("OLYMPIC.INP","r",stdin);
    freopen("OLYMPIC.OUT","w",stdout);
    solve();
    return 0;
}
