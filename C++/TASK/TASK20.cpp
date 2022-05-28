#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int x = 1;
    int S = 0;
    int m = sqrt(n);
    while (x <= m)
    {
        if (n % x == 0)
        {
            S += x + (n / x);
        }
        x += 1;
    }
    if (m * m == n)
    {
        S -= m;
    }
    return S;
}

int main()
{
    freopen("TASK20.INP","r",stdin);
    freopen("TASK20.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
