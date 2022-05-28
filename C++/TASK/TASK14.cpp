#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int x = abs(n);
    int S = 0;
    int i = 0;
    while(x != 0)
    {
        if(i % 2 == 0)
        {
            S += x % 10;
        }
        x /= 10;
        i += 1;
    }
    return S;
}

int main()
{
    freopen("TASK14.INP","r",stdin);
    freopen("TASK14.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
