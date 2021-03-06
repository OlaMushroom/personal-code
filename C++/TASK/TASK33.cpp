#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int func (int n)
{
    int i = 0;
    int x = 0;
    int S = 9;
    int m = 0;
    while (n != 0)
    {
        x = n % 10;
        if (x != 0 && x < S)
        {
            S = x;
            m = i;
        }
        i++;
        n /= 10;
    }
    return m;
}

int main()
{
    freopen("TASK33.INP","r",stdin);
    freopen("TASK33.OUT","w",stdout);
    int n;cin>>n;
    int out = func(n);
    cout<<out;
    return 0;
}
