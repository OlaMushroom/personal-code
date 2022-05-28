#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;
vector<long long> a; int n;
long long m = pow(10,9) + 7;

void input ()
{
    cin>>n; a.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
}

void arithmetic ()
{
    while (n > 0)
    {
        for (int i = 0; i < (n - 1); ++i)
        {
            a[i] = (a[i] + a[i + 1]) % m;
        }
        n -= 1;
        for (int i = 0; i < (n - 1); ++i)
        {
            a[i] = (a[i] * a[i + 1]) % m;
        }
        n -= 1;
    }
    cout<<a[0];
}

int main()
{
    freopen("ARITHMETIC.INP","r",stdin);
    freopen("ARITHMETIC.OUT","w",stdout);
    input(); arithmetic();
    return 0;
}
