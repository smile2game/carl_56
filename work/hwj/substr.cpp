#include <bits/stdc++.h>
using namespace std;

static inline bool isSubsequence(const string& A, const string& B) {
    // 判定 B 是否为 A 的子序列
    size_t j = 0;
    for (char c : A) {
        if (j < B.size() && c == B[j]) ++j;
        if (j == B.size()) return true; // 提前结束
    }
    return j == B.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    for (int k = 0; k < N; ++k) {
        string A, B;
        cin >> A >> B;        // 输入保证无空格字符，用 >> 即可
        cout << (isSubsequence(A, B) ? "SUB" : "NO") << '\n';
    }
    return 0;
}
