#include <bits/stdc++.h>
#include <vector>
#define arrMAX 100000
using namespace std;

int n, h[arrMAX], m[arrMAX];

void input ()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> h[i] >> m[i];
        m[i] += (h[i] * 60);
    }
}

void solve ()
{
    input(); sort(m, m+n);
    int v = m[0], f = 1, cnt = 1;
    for (int i = 1; i < n; i++)
    {
        if (m[i] == v)
        {
            f++;
            if (f > cnt) cnt = f;
        }
        else
        {
            v = m[i];
            f = 1;
        }
    }
    cout << cnt;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("FREECASH.INP","r",stdin);
    freopen("FREECASH.OUT","w",stdout);
    solve();
    return 0;
}
