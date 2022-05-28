#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int a[1000000], n;

void input()
{
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
    }
}

void prime()
{
    int S = abs(a[0] - a[1]);
    for (int i = 1; i < (n - 1); ++i)
    {
        int m = abs(a[i] - a[i + 1]);
        if (m < S)
        {
            S = m;
        }
    }
    cout<<S;
}

int main()
{
    freopen("MANG02.INP","r",stdin);
    freopen("MANG02.OUT","w",stdout);
    input();prime();
    return 0;
}
