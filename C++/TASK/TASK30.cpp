#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap (int n)
{
    int i = 0;
    int S = 0;
    while (n != 0)
    {
        i = n % 10;
        if (i > S)
        {
            S = i;
        }
        n /= 10;
    }
    return S;
}

int main()
{
    freopen("TASK30.INP","r",stdin);
    freopen("TASK30.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
