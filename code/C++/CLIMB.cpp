#include <iostream>
#include <cstdio>

using namespace std;
int a[1000000]; int n;

void input ()
{
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
}

void climb ()
{
    int x = a[0], m = 0, S = 0;
    for (int i = 1; i <= n; ++i)
    {
        if (a[i] <= a[i - 1])
        {
            m = a[i - 1] - x;
            if (m > S) S = m;
            x = a[i];
        }
    }
    cout<<S;
}

int main()
{
    freopen("CLIMB.INP","r",stdin);
    freopen("CLIMB.OUT","w",stdout);
    input(); climb();
    return 0;
}
