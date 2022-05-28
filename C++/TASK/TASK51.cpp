#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    for(int i = 1;i <= n;i++)
    {
        for(int S = 1;S <= i;S++)
        {
            cout<<"* ";
        }
        cout<<"\n";
    }
}

int main()
{
    freopen("TASK51.INP","r",stdin);
    freopen("TASK51.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
