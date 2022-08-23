#include <iostream>
#include <set>
#include <vector>

using namespace std;

set<long> visited;

vector<vector<bool>> matrix;
int n;

long long dfs(long start) {
    visited.insert(start);

    long long total = 1;
    for (long i = 0; i < n; i++)
    {
        if (matrix[start][i] == 1 && visited.find(i) == visited.end()) {
            total += dfs(i);
        }
    }

    return total;
}

int main()
{
    int t;
    cin >> t;
    long long MOD = 1000000000;
    while (t)
    {
        long long m;
        cin >> n >> m;
        matrix.clear();
        for (long i = 0; i < n; i++) {
            vector<bool> temp;
            for (long j = 0; j < n; j++) {
                temp.push_back(0);
            }
            matrix.push_back(temp);
        }
        long x, y;
        for (long i = 0; i < m; i++) {
            cin >> x >> y;
            matrix[x - 1][y - 1] = 1;
            matrix[y - 1][x - 1] = 1;
        }

        visited.clear();
        long long answer0 = 0;
        long long answer1 = 1;
        for (int i = 0; i < n; i++)
        {
            if (visited.find(i) == visited.end())
            {
                answer1 = (answer1 * (dfs(i)) % MOD) % MOD;
                answer0 += 1;
            }
        }

        cout << answer0 % MOD << ' ' << answer1 << endl;

        t -= 1;
    }
    

    return 0;
}
