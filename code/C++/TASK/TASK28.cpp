#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (long long n)
{
    long long i = 1;
    long long S = 0;
    while (S <= n)
    {
        S = i*i;
        if (S <= n)
        {
            cout<<S<<"\n";
        }
        i++;
    }
}

int main()
{
    freopen("TASK28.INP","r",stdin);
    freopen("TASK28.OUT","w",stdout);
    long long n;cin>>n;
    func(n);
    return 0;
}
