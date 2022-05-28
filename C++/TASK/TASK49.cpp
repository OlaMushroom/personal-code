#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int hcf (int x, int y)
{
    int a = x;
    int b = y;
    while (b != 0)
    {
        int c = a % b;
        a = b; b = c;
    }
    return a;
}

bool check (int i)
{
    int m = i;
    int x = 0;
    int y = m % 10;
    while (m > 0)
    {
        x = m % 10;
        y = hcf(x,y);
        m /= 10;
    }
    return (y == 1);
}

int func (int n)
{
    int cnt = 0;
    for (int i = 1; i <= n; ++i)
    {
        if (check(i) == 1)
        {
            cnt++;
        }
    }
    return cnt;
}

int main()
{
    freopen("TASK49.INP","r",stdin);
    freopen("TASK49.OUT","w",stdout);
    int n;cin>>n;
    int out = func(n);
    cout<<out;
    return 0;
}
