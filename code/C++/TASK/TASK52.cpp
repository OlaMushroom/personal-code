#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int n)
{
    int m = n;
    for(int i = 1;i <= n;i++)
    {
        for(int S = m;S > 1;S--)
        {
            cout<<"  ";
        }
        for(int x = 1;x <= i;x++)
        {
            cout<<"* ";
        }
        m--;
        cout<<"\n";
    }
}

int main()
{
    freopen("TASK52.INP","r",stdin);
    freopen("TASK52.OUT","w",stdout);
    int n;cin>>n;
    func(n);
    return 0;
}
