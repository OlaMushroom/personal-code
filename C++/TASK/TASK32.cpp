#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap (int n)
{
    int i = 0;
    int S = 10;
    int m = -1;
    while (n != 0)
    {
        if (n % 2 != 0)
            {
                i = n % 10;
                if (i < S)
                {
                    S = i;
                }
            }
        n /= 10;
    }
    if (S == 10)
    {
        return m;
    }
    else
    {
        return S;
    }
}

int main()
{
    freopen("TASK32.INP","r",stdin);
    freopen("TASK32.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
