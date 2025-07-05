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
    int n,m;
    cin>>n>>m;
    vector<int>v(n);
    int total = 0;
    for(auto it:v){
        cin>>it;
        total+=it;
    }
    if(total<=m){
        yes;
        return;
    }
    no;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t(1);
    //cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
