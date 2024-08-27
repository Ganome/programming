// Demonstrates how to declare functions
#include <iostream>

int Area(int length, int width); // A function prototype because it ends with a semicolon

int main()
{
    using namespace std;

    int lengthOfYard, widthOfYard, areaOfYard;

    cout << "\nHow wide is your yard? ";
    cin >> widthOfYard;
    cout << "\nHow long is your yard? ";
    cin >> lengthOfYard;

    areaOfYard = Area(lengthOfYard, widthOfYard);

    cout << "\nYour yard is " << areaOfYard << " square feet!\n\n";
    return 0;
}

int Area(int len, int wid)
{
    return len * wid;
}