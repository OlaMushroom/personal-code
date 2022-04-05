#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;
int a[2000000], n, m;

void input ()
{
    cin>>n>>m;
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
        a[i + n] = a[i];
    }
}

void output ()
{
    int k = m % n;
    for (int i = k; i < k + n; ++i)
    {
        cout<<a[i]<<" ";
    }
}

int main()
{
    freopen("MANG10.INP","r",stdin);
    freopen("MANG10.OUT","w",stdout);
    input();output();
    return 0;
}
