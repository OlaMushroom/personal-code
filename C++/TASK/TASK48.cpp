#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

bool check (int m)
{
    int cnt = 0;
    for(int i = 2; i <= sqrt(m); i++)
    {
        if(m % i == 0)
        {
            cnt++;
        }
    }
    return (cnt == 0);
}

void primea (int n)
{
    for (int a = (n - 1); a > 1; a--)
    {
        int m = a;
        if (check(m) == 1)
        {
            cout<<a;
            break;
        }
    }
    cout<<"\n";
}

void primeb (int n)
{
    for (int b = (n + 1); b > n; b++)
    {
        int m = b;
        if (check(m) == 1)
        {
            cout<<b;
            break;
        }
    }
}

int main()
{
    freopen("TASK48.INP","r",stdin);
    freopen("TASK48.OUT","w",stdout);
    int n;cin>>n;
    primea(n);primeb(n);
    return 0;
}
