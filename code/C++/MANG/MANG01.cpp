#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int a[1000000], n, x;

void input()
{
    cin>>n>>x;
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
    }
}

void factor()
{
    int cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] != 0)
            if (x % a[i] == 0)
            {
                cnt++;
            }
    }
    cout<<cnt;
}

int main()
{
    freopen("MANG01.INP","r",stdin);
    freopen("MANG01.OUT","w",stdout);
    input();factor();
    return 0;
}
