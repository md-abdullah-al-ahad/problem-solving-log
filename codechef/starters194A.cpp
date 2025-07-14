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

void solve()
{
    int n;
    cin>>n;
    vector<int>v(n);
    for(auto &it:v) cin>>it;
    int ans = min(v[0],v[n-1]);
    for(int i = 1;i<n-1;i++){
        ans = min(ans,v[i]+v[i+1]);
    }
    for(int i = 1;i<n-1;i++){
        ans = min(ans,v[i-1]+v[i]);
    }
    cout<<ans<<"\n";
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
