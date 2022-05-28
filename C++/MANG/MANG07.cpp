#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int a[1000000], n;

void input ()
{
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
    }
}

void output ()
{
    cout<<a[0]<<" ";
    for (int i = 1; i < n; ++i)
    {
        if (a[i - 1] > a[i])
        {
            cout<<"\n";
        }
        cout<<a[i]<<" ";
    }
}

int main()
{
    freopen("MANG07.INP","r",stdin);
    freopen("MANG07.OUT","w",stdout);
    input();output();
    return 0;
}
