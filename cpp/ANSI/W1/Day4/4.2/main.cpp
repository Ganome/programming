// Demonstration of subtraction and Interger Overflow
#include <iostream>

using namespace std;

int main()
{
    typedef unsigned int UINT;
    UINT difference;
    UINT bigNumber = 100;
    UINT smallNumber = 50;

    difference = bigNumber - smallNumber;
    cout << "Difference is: " << difference;

    difference = smallNumber - bigNumber;
    cout << "\nNow the difference is: " << difference << endl;
    return 0;
}