#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (long long n)
{
    long long a = 2;
    long long m = sqrt(n);
    while (n > 1 && a <= m)
    {
        if (n % a == 0)
        {
            while (n % a == 0)
            {
                n /= a;
            }
            cout<<a<<" ";
        }
        a++;
    }
    if (n > 1)
    {
        cout << n << " ";
    }
}

int main()
{
    freopen("TASK38.INP","r",stdin);
    freopen("TASK38.OUT","w",stdout);
    long long n;cin>>n;
    func(n);
    return 0;
}
