#include <iostream>
#include <cstring>
#include <string>
using namespace std;

struct Stack
{
    int data[10000];
    int size;
    Stack()
    {
        size = 0;
    }

    void push(int num)
    {
        data[size] = num;
        size += 1;
    }
    bool empty()
    {
        if (size == 0)
            return true;
        else
            return false;
    }

    int pop()
    {
        if (empty())
            return -1;
        else
        {
            size -= 1;
            return data[size];
        }
    }

    int top()
    {
        if (empty())
            return -1;
        else
            return data[size - 1];
    }
};

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("stack.txt", "r", stdin);
    int N;
    cin >> N;
    Stack s;
    for (int i = 0; i < N; i++)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "push")
        {
            int num;
            cin >> num;
            s.push(num);
        }
        else if (cmd == "top")
        {
            cout << (s.empty() ? -1 : s.top()) << '\n';
        }
        else if (cmd == "size")
        {
            cout << s.size << '\n';
        }
        else if (cmd == "empty")
        {
            cout << s.empty() << '\n';
        }
        else if (cmd == "pop")
        {
            cout << (s.empty() ? -1 : s.top()) << '\n';
            if (!s.empty())
            {
                s.pop();
            }
        }
    }
    return 0;
}