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

int prime()
{
    int S = 0;
    for (int i = 0; i < n; ++i)
    {
        if (check(a[i]) == 1)
        {
            if (a[i] > S)
            {
                S = a[i];
            }
        }
    }
    return S;
}

void fnd()
{
    int S = prime();
    if (S != 0)
    {
        for (int i = 0; i < n; i++)
        {
            if (a[i] == S)
            {
                cout<<i+1;
                break;
            }
        }
    }
    else
    {
        cout<<"-1";
    }
}

int main()
{
    freopen("MANG06.INP","r",stdin);
    freopen("MANG06.OUT","w",stdout);
    input();fnd();
    return 0;
}
