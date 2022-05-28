#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    for(int i = 1;i <= n;i++)
    {
        for(int S = 1;S <= (n - i);S++)
        {
            cout<<" ";
        }
        for(int x = 1;x <= i;x++)
        {
            cout<<"* ";
        }
        cout<<"\n";
    }
}

int main()
{
    freopen("TASK55.INP","r",stdin);
    freopen("TASK55.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
