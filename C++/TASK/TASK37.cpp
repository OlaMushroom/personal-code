#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    int a = 2;
    int m = n;
    while (n > 1 && a <= m)
    {
        if (n % a == 0)
        {
            cout<<a<<" ";
            n /= a;
        }
        else
        {
            a++;
        }
    }
    if (n > 1)
    {
        cout << n << " ";
    }
}

int main()
{
    freopen("TASK37.INP","r",stdin);
    freopen("TASK37.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
