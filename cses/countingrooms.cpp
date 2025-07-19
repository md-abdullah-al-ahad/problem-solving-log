#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<ll, ll> pi;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define endl "\n"
#define yes cout << "Yes" << endl
#define no cout << "No" << endl
#define rep(i, a, b) for (ll i = a; i < b; i++)
void dfs(vector<vector<char>> &ar, vector<vector<int>> &vis, int i, int j, int n, int m)
{
    if (i < 0 || i >= n || j < 0 || j >= m)
        return;
    if (ar[i][j] == '#' || vis[i][j] == 1)
        return;
    vis[i][j] = 1;
    dfs(ar, vis, i + 1, j, n, m);
    dfs(ar, vis, i - 1, j, n, m);
    dfs(ar, vis, i, j + 1, n, m);
    dfs(ar, vis, i, j - 1, n, m);
}
void solve()
{
    int n, m;
    cin >> n >> m;
    vector<vector<char>> ar(n, vector<char>(m));
    vector<vector<int>> vis(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> ar[i][j];
        }
    }
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (vis[i][j] == 0 && ar[i][j] == '.')
            {
                total++;
                dfs(ar, vis, i, j, n, m);
            }
        }
    }
    cout<<total<<"\n";
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t(1);
    // cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
