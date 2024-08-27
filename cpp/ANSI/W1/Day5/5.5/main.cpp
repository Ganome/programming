/* Further demonstration of global and local variables */
#include <iostream>

using namespace std;

void myFunction();

int x = 5, y = 7;       // Global variables

int main()
{
    cout << "x from main: " << x << endl;
    cout << "y from main: " << y << endl;
    myFunction();
    cout << "Back from myFunction!" << endl << endl;
    cout << "x from main: " << x << endl;
    cout << "y from main: " << y << endl;
    return 0;
}

void myFunction()
{
    int y = 10;

    cout << "x from myFunction: " << x << endl;
    cout << "y from myFunction: " << y << endl << endl;
}