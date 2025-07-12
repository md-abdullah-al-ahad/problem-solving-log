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
#define yes cout << "Yes" << endl;
#define no cout << "No" << endl;
#define rep(i, a, b) for (ll i = a; i < b; i++)

vector<ll> pal(ll N)
{
    vector<ll> result;
    for (int l = 1; l <= 12; l++)
    {
        int halfl = (l + 1) / 2;
        ll start;
        if (l == 1)
            start = 1;
        else
            start = pow(10, halfl - 1);
        ll end = pow(10, halfl);
        for (ll i = start; i < end; ++i)
        {
            string half = to_string(i);
            string full = half;
            if (l % 2 == 1)
                half.pop_back();
            reverse(half.begin(), half.end());
            full += half;
            ll p = stoll(full);
            if (p > N)
                return result;
            result.push_back(p);
        }
    }
    return result;
}
bool otherpal(ll n, ll A)
{
    if (n == 0)
        return true;

    string s;
    while (n > 0)
    {
        s += (n % A) + '0';
        n /= A;
    }
    string s1 = s;
    reverse(s.begin(), s.end());
    return s == s1;
}
void solve()
{
    ll N = 1000000000000;
    vector<ll> result = pal(N);
    ll a, n;
    cin >> a >> n;
    ll total = 0;
    for (ll i = 0; i < result.size(); i++)
    {
        if (result[i] > n)
        {
            break;
        }
        if (otherpal(result[i], a))
        {
            total += result[i];
        }
    }
    cout << total << "\n";
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t(1);
    // cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
