
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

bool check(string prev, string now){
    return prev.at(prev.size()) == now.at(0);
}
bool eq(string ele, vector<string> comp2) {
    for (int i=0; i<comp2.size();i++) {
        if (ele == comp2.at(i)) {
            return true;
        }
    }
    return false;
}
int N;
vector<string> round;
int main() {
    string temp;
    cin >> N;
    for (int i =0; i<N; i++) {
        cin >> temp;
        round.push_back(temp);
    }
    string prev = round.at(0);
    for (int j=1; j<N-1; j++) {
        if (!(check(prev, round.at(j))) || eq(round.at(j), round)) {
            cout << "Player " << j%2+1 << " lost";
            return 0;
        }
    }
    cout << "Fair Game";

}




