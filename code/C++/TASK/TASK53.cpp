#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    int i,S,m;
    int x = n;
    for(i = 1;i <= n;i++)
    {
        for(S = x;S >= 1;S--)
        {
            cout<<"* ";
        }
        cout<<"\n";
        for(m = 1;m <= i;m++)
        {
            cout<<"  ";
        }
        x--;
    }
}

int main()
{
    freopen("TASK53.INP","r",stdin);
    freopen("TASK53.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
