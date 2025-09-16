#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L, N;
    cin >> L >> N;
    vector<int> data(L);
    for (int i = 0; i < L; i++) cin >> data[i];

    vector<int> cnt(201, 0);
    for (int i = 0; i < N; i++) cnt[data[i]]++;

    auto getMedian = [&](const vector<int>& cnt) -> double {
        int total = N;
        int half1 = (total + 1) / 2; // for odd or first middle
        int half2 = (total % 2 == 0) ? (total / 2 + 1) : half1;
        int sum = 0;
        int m1 = -1, m2 = -1;
        for (int v = 0; v <= 200; v++) {
            sum += cnt[v];
            if (m1 == -1 && sum >= half1) m1 = v;
            if (m2 == -1 && sum >= half2) {
                m2 = v;
                break;
            }
        }
        return (m1 + m2) / 2.0;
    };

    int alerts = 0;
    for (int i = N; i < L; i++) {
        double median = getMedian(cnt);
        if (data[i] >= 2 * median) alerts++;
        // 滑动窗口：移除 data[i-N]，加入 data[i]
        cnt[data[i - N]]--;
        cnt[data[i]]++;
    }

    cout << alerts << "\n";
    return 0;
}
