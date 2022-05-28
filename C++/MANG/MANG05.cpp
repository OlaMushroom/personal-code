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
    int x = 0;
    for (int i = 0; i < a.size(); ++i)
    {
        if (i != m)
        {
            if (a[i] < S)
            {
                S = a[i];
                x = i;
            }
        }
    }
    return x+1;
}

void output()
{
    int n1 = minNum(-1);
    int n2 = minNum(n1-1);
    cout<<n1<<" "<<n2;
}

int main()
{
    freopen("MANG05.INP","r",stdin);
    freopen("MANG05.OUT","w",stdout);
    input();output();
    return 0;
}
