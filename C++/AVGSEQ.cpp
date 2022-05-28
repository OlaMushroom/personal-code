#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;
vector<long long> a;
vector<long long> b;
int n;

void input ()
{
    cin>>n;
    a.resize(n);
    b.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin>>b[i];
        b[i] *= i + 1;
    }

}

void avgseq ()
{
    a[0] = b[0]; cout<<a[0]<<" ";
    for (int i = 1; i < n; ++i)
    {
        a[i] = b[i] - b[i - 1];
        cout<<a[i]<<" ";
    }
}

int main()
{
    freopen("AVGSEQ.INP","r",stdin);
    freopen("AVGSEQ.OUT","w",stdout);
    input(); avgseq();
    return 0;
}
