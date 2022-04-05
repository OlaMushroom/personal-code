#include <iostream>
#include <cstdio>
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
    int cnt = 0;
    int S = 0;
    for (int i = 0; i < n; ++i)
    {
        cnt++;
        if (cnt > S)
        {
            S = cnt;
        }
        if (a[i] > a[i + 1])
        {
            cnt = 0;
        }
    }
    cout<<S;
}

int main()
{
    freopen("MANG08.INP","r",stdin);
    freopen("MANG08.OUT","w",stdout);
    input();output();
    return 0;
}
