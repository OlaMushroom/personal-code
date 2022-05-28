#include <bits/stdc++.h>
#include <vector>
#define arrMAX 10000
using namespace std;

int n, m, S, a, b, t[arrMAX];
int check[arrMAX] = {false};

void solve ()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> t[i];
        S += t[i];
    }
    for (int i = 1; i <= m; i++)
    {
        cin >> a >> b;
        check[a] = true;
    }
    int x = 0;
    for (int i = 1; i <= n; i++)
    {
        if (check[i] == 0) x = max(x, t[i]);
    }
    cout << (S -= x);
}

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("HOMEWORK.INP","r",stdin);
    freopen("HOMEWORK.OUT","w",stdout);
    solve();
    return 0;
}
