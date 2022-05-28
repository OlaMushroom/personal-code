#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int func (int n)
{
    int i = 0;
    int S = 9;
    while (n != 0)
    {
        i = n % 10;
        if (i != 0 && i < S)
        {
            S = i;
        }
        n /= 10;
    }
    return S;
}

int main()
{
    freopen("TASK29.INP","r",stdin);
    freopen("TASK29.OUT","w",stdout);
    int n;cin>>n;
    int a = func(n);
    cout<<a;
    return 0;
}
