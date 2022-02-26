#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    for(int i = 1;i <= n;i++)
    {
        for(int S = 1;S <= 2*(n - i);S+=2)
        {
            cout<<"  ";
        }
        for(int x = 1;x <= (2*i)-1;x++)
        {
            cout<<"* ";
        }
        cout<<"\n";
    }
}

int main()
{
    freopen("TASK56.INP","r",stdin);
    freopen("TASK56.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
