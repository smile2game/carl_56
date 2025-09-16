#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

const int MAX_HEIGHT = 1e5 + 5;
vector<int> sg(MAX_HEIGHT, 0);

// 预计算所有可能高度的SG值
void precomputeSG() {
    sg[1] = 0;  // 高度为1的塔无法拆分，SG值为0
    
    for (int x = 2; x < MAX_HEIGHT; ++x) {
        unordered_set<int> reachable;
        
        // 找出所有可能的拆分方式 Y*Z = x, Y > 1
        for (int Y = 2; Y * Y <= x; ++Y) {
            if (x % Y == 0) {
                int Z = x / Y;
                
                // 拆分方式1: Y个高度为Z的塔
                if (Y % 2 == 1) {
                    reachable.insert(sg[Z]);
                } else {
                    reachable.insert(0);  // 偶数个相同SG值的异或为0
                }
                
                // 拆分方式2: Z个高度为Y的塔（如果Y != Z且Z > 1）
                if (Y != Z && Z > 1) {
                    if (Z % 2 == 1) {
                        reachable.insert(sg[Y]);
                    } else {
                        reachable.insert(0);  // 偶数个相同SG值的异或为0
                    }
                }
            }
        }
        
        // 计算mex（最小的未出现的非负整数）
        int mex = 0;
        while (reachable.count(mex)) {
            mex++;
        }
        sg[x] = mex;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    precomputeSG();  // 预计算所有SG值
    
    int T;
    cin >> T;
    
    while (T--) {
        int N;
        cin >> N;
        
        vector<int> heights(N);
        for (int i = 0; i < N; ++i) {
            cin >> heights[i];
        }
        
        // 计算所有塔的SG值的异或
        int xor_total = 0;
        for (int h : heights) {
            xor_total ^= sg[h];
        }
        
        // 判断胜负：异或结果非0则玩家1胜，否则玩家2胜
        cout << (xor_total != 0 ? 1 : 2) << "\n";
    }
    
    return 0;
}
