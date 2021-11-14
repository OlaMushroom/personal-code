#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int S = 0;
    int i = 0;
    while(n != 0)
    {
        S = n % 10;
        if(S != 0)
        {
            i += 1;
        }
        n /= 10;
    }
    return i;
}

int main()
{
    freopen("TASK12.INP","r",stdin);
    freopen("TASK12.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
