#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int i = 0;
    int m = 0;
    int S = 0;
    int x = abs(n);
    while (x != 0)
    {
        i = x % 10;
        m = m * 10 + i;
        x /= 10;
    }
    if (n > 0)
    {
        S = n + m;
    }
    else
    {
        S = n - m;
    }
    return S;
}

int main()
{
    freopen("TASK22.INP","r",stdin);
    freopen("TASK22.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
