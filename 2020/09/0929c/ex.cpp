#include <iostream>
using namespace std;
long long mul(long long a, long long b, long long c)
{
    if (b == 0)
    {
        return 1LL;
    }
    else if (b == 1)
    {
        return a % c;
    }
    else if (b % 2 == 0)
    {
        long long temp = mul(a, b / 2, c) % c;
        return (temp * temp) % c;
    }
    else
    {
        return (a * mul(a, b / 2, c)) % c;
    }
}

int main()
{
    freopen("1629.txt", "r", stdin);
    long long a, b, c;
    cin >> a >> b >> c;
    cout << mul(a, b, c) << "\n";
    return 0;
}