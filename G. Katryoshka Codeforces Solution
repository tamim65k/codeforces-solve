#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, m, k;
    cin >> n >> m >> k;

    long long case1 = min({n, m, k});

    n -= case1;
    m -= case1;
    k -= case1;

    long long case2 = min(n / 2, k);

    n -= 2 * case2;
    k -= case2;

    long long case3 = min({n / 2, m, k});

    long long maxKatryoshkas = case1 + case2 + case3;
    cout << maxKatryoshkas << endl;

    return 0;
}
