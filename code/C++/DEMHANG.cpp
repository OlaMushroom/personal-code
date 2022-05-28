#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
int arr[1000000], val[1000000], freq[1000000], n;

void input ()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
}

void demhang ()
{
    sort(arr, arr + n);
    int order, m = 0, x = 0;
    val[0] = arr[0]; freq[0] = 1;
    for (int i = 1; i < n; ++i)
    {
        if (arr[i] != arr[i - 1])
        {
            m++;
            val[m] = arr[i];
            freq[m] = 1;
        }
        else freq[m]++;
    }
    for (int j = 0; j < n; ++j)
    {
        if (x < freq[j])
        {
            x = freq[j];
            order = j;
        }
    }
    cout << val[order] << " " << freq[order];
}

int main()
{
    freopen("DEMHANG.INP","r",stdin);
    freopen("DEMHANG.OUT","w",stdout);
    input(); demhang();
    return 0;
}
