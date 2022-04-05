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
        int x = sqrt(a[i]);
        cnt++;
        if (x*x == a[i])
        {
            if (cnt > S)
            {
                S = cnt;
            }
        }
        else
        {
            cnt = 0;
        }
    }
    cout<<S;
}

int main()
{
    freopen("MANG09.INP","r",stdin);
    freopen("MANG09.OUT","w",stdout);
    input();output();
    return 0;
}
