#include <iostream>
#include <cstring>
using namespace std;
// 11758

int ccw(int x1, int y1, int x2, int y2, int x3, int y3)
{
    int temp = x1 * y2 + x2 * y3 + x3 * y1;
    temp -= y1 * x2 + y2 * x3 + y3 * x1;
    if (temp > 0)
        return 1;
    else if (temp < 0)
        return -1;
    else
        return 0;
}

int main()
{
    freopen("ccw.txt", "r", stdin);
    int x1, y1, x2, y2, x3, y3;
    scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);
    printf("%d\n", ccw(x1, y1, x2, y2, x3, y3));
    return 0;
}