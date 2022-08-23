#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string ArrayChallenge(int arr[])
{
    return min(arr[1], arr[3]) - max(arr[0], arr[2]) + 1 >= arr[4] ? "true" : "false";
}

int main()
{
    int arr[5] = {0};
    for (int i = 0; i < 5; i += 1)
    {
        cin >> arr[i];
    }
    cout << ArrayChallenge(arr) << endl;
}