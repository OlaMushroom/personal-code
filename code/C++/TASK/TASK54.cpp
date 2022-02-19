#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    for(int i = 1;i <= n;i++)
    {
        int S;
        for(S = i;S <= n;S++)
        {
            cout<<" *";
        }
        cout<<"\n";
    }
}

int main()
{
    freopen("TASK54.INP","r",stdin);
    freopen("TASK54.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
