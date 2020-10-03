#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> &v)
{
    for (auto i : v)
    {
        cout << i << " ";
    }
}

vector<int> preprocessing(string p)
{
    int m = p.size();
    vector<int> pi(m);
    pi[0] = 0;
    int j = 0;
    for (int i = 1; i < m; i++)
    {
        while (j > 0 && p[i] != p[j])
        {
            j = pi[j - 1];
        }
        if (p[i] == p[j])
        {
            pi[i] = j + 1;
            j++;
        }
        else
        {
            pi[i] = 0;
        }
    }
    return pi;
}

vector<int> kmp(string s, string p)
{
    auto pi = preprocessing(p);
    vector<int> ans;
    int n = s.size(), m = p.size(), i, j = 0;
    for (int i = 0; i < n; i++)
    {
        while (j > 0 && s[i] != p[j])
        {
            j = pi[j - 1];
        }
        if (s[i] == p[j])
        {
            if (j == m - 1)
            {
                ans.push_back(i - m + 1);
                j = pi[j];
            }
            else
            {
                j++;
            }
        }
    }
}

int main()
{
    freopen("kmp.txt", "r", stdin);
    string s;
    cin >> s;
    vector<int> pi = preprocessing(s);
    cout << s << endl;
    print(pi);
    return 0;
}