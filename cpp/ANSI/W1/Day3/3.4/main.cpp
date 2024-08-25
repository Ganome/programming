// Demonstrating buffer overflow with unsigned short int
#include <iostream>

int main()
{
    using namespace std;

    unsigned short int smallNumber = 65535;
    cout << "small number:\t" << smallNumber << endl;
    smallNumber++;
    cout << "small number:\t" << smallNumber << endl;
    smallNumber++;
    cout << "small number:\t" << smallNumber << endl;

    return 0;
}