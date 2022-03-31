#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;
vector<int> a; int n;

void input()
{
    cin>>n;
    a.resize(n);
    for (int i = 0; i < n; ++i)
    {
        cin>>a[i];
    }
}

int minNum (int m)
{
    int S = a[0];
    for (int i = 0; i < a.size(); ++i)
    {
        if (a[i] != m)
        {
            if (a[i] < S)
            {
                S = a[i];
            }
        }
    }
    return S;
}

void output()
{
    int n1 = minNum(-1);
    int n2 = minNum(n1);
    cout<<n1<<" ";
    if (n2 != n1)
    {
        cout<<n2;
    }
    else
    {
        cout<<"-1";
    }
}

int main()
{
    freopen("MANG04.INP","r",stdin);
    freopen("MANG04.OUT","w",stdout);
    input();output();
    return 0;
}
