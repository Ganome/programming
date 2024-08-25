// Demonstrating another overflow for a signed short int
#include <iostream>

int main()
{
    using namespace std;

    short int smallNumber = 32767;

    cout << "small number:\t" << smallNumber << endl;
    smallNumber++;
    cout << "small number:\t" << smallNumber << endl;
    smallNumber++;
    cout << "small number:\t" << smallNumber << endl;

    return 0;
}