#include <iostream>

using namespace std;


long long getMaxTickets(long long intervals[][2], long long N) {
    long long low = intervals[0][0];
    long long high = intervals[0][1];
    long long l, h;
    for (long long i = 1; i < N; i++) {
        l = intervals[i][0];
        h = intervals[i][1];
        if (l > high || h < low) {
            return 0;
        }
        else {
            if (l > low) low = l;
            if (h < high) high = h; 
        }
        cout << low << ' ' << high << endl;
    }
    return high - low + 1;
}


int main() {
    long long N;
    long long M;
    cin >> N >> M;
    long long intervals[M][2];
    long long l, h;
    for (long long i = 0; i < M; i++)
    {
        cin >> l >> h;
        intervals[i][0] = l;
        intervals[i][1] = h;
    }
    cout << getMaxTickets(intervals, M) << endl;
}