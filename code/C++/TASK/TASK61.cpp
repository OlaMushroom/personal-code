#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void func (int x,int y)
{
    int a,b;
    int z = 0;
    for (a = 1;a <= sqrt(y);a++)
    {
        if (y % a == 0)
        {
            b = y / a;
            if (x == 2*(a + b))
            {
                z = 1;
                cout<< a << " " << b;
            }
        }
    }
    if (z != 1)
    {
        cout<<"-1";
    }
}

int main()
{
    freopen("TASK61.INP","r",stdin);
    freopen("TASK61.OUT","w",stdout);
    int x;int y;
    cin>>x>>y;
    func(x,y);
    return 0;
}
