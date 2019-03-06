#include <iostream>

using namespace std;


/**
 * @brief calculate greatest common factor for a and b
 * @param a int
 * @param b int
 * @return int
 */
int greatest_common_factor(int a, int b) {
    while(b != 0) {
        int reminder = a % b;
        a = b;
        b = reminder;
    }
    return a;
}


int main(){
    cout << greatest_common_factor(8, 16) << endl;
    return 0;
}
