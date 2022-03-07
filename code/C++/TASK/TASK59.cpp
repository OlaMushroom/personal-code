#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int func (int n, int a, int b)
{
    int i = 0;
    int m;
    for (m = 1; m <= n; m++)
    {
        if (m % a == 0 && m % b == 0)
        {
            i++;
        }
    }
    return i;
}

int main()
{
    freopen("TASK59.INP","r",stdin);
    freopen("TASK59.OUT","w",stdout);
    int n; int a; int b;
    cin>>n>>a>>b;
    int out = func(n,a,b);
    cout<<out;
    return 0;
}
