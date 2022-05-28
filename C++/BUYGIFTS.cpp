#include <bits/stdc++.h>
#include <vector>
#define arrMAX 100000
using namespace std;

int n, m; long long a[arrMAX];

void solve ()
{
    cin >> n >> m; m--;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort (a, a+n);
    long long x = a[m] - a[0];
    for (int i = 1; i < (n - m); i++)
    {
        x = min(x, a[i + m] - a[i]);
    }
    cout << x;
}

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("BUYGIFTS.INP","r",stdin);
    freopen("BUYGIFTS.OUT","w",stdout);
    solve();
    return 0;
}
