#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
long long a[100000], n;

void disnum ()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort(a, a+n); int cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] != a[i + 1]) cnt++;
    }
    cout << cnt;
}

int main()
{
    freopen("DISNUM.INP","r",stdin);
    freopen("DISNUM.OUT","w",stdout);
    disnum();
    return 0;
}
