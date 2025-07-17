#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<ll, ll> pi;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define endl "\n";
#define yes cout << "Yes" << endl;
#define no cout << "No" << endl;
#define rep(i, a, b) for (ll i = a; i < b; i++)

void solve()
{
    int n, k;
    cin >> n >> k;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    int myval = v[k - 1];
    sort(v.begin(), v.end());
    int starting = -1;
    for (int i = 0; i < n; i++)
    {
        if (myval == v[i])
        {
            starting = i;
        }
    }

    int current = 1;
    for (int i = starting; i < n - 1; i++)
    {
        int t = v[i + 1] - v[i];
        current = current + t;
        if (current > myval + 1)
        {
            no;
            return;
        }
        myval = v[i + 1];
    }
    yes;
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t(1);
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
