#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int a[1000000], n;

void input()
{
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
    }
}

bool check (int m)
{
    if (m < 2)
    {
        return false;
    }
    for(int i = 2; i <= sqrt(m); ++i)
    {
        if(m % i == 0)
        {
            return false;
        }
    }
    return true;
}

void prime()
{
    int cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        if (check(a[i]) == 1)
        {
            cnt++;
        }
    }
    cout<<cnt;
}

int main()
{
    freopen("MANG03.INP","r",stdin);
    freopen("MANG03.OUT","w",stdout);
    input();prime();
    return 0;
}
