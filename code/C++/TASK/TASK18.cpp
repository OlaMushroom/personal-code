#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int i = 0;
    int x = 1;
    int m = sqrt(n);
    while (x <= m)
    {
        if (n % x == 0)
        {
            i += 2;
        }
        x += 1;
    }
    if (m * m == n)
    {
        i -= 1;
    }
    return i;
}

int main()
{
    freopen("TASK18.INP","r",stdin);
    freopen("TASK18.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
