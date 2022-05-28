#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int baitap(int n)
{
    int i = abs(n);
    int S = 1;
    while(i != 0)
    {
        if(i % 2 != 0)
        {
            S *= i % 10;
        }
        i /= 10;
    }
    return S;
}

int main()
{
    freopen("TASK15.INP","r",stdin);
    freopen("TASK15.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
