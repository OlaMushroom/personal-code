#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int i = 0;
    int S = 0;
    while (n != 0)
    {
        i = n % 10;
        S = S * 10 + i;
        n /= 10;
    }
    return S;
}

int main()
{
    freopen("TASK16.INP","r",stdin);
    freopen("TASK16.OUT","w",stdout);
    int n;
    cin>>n;
    int m = baitap(n);
    cout<<m;
    return 0;
}
