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
    string s;
    cin>>s;
    if(n<=2){
        no;
        return;
    }
    if(s[n-1]=='a' && s[n-2]=='e' && s[n-3]=='t'){
        yes;
        return;
    }
    no;
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t(1);
    //cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
