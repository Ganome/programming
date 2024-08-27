/* Demonstrates how variables defined inside functions
are only available inside that function*/
#include <iostream>

float Convert(float);
int main()
{
    using namespace std;

    float TempFer;
    float TempCel;

    cout << "Please enter the temperature in Fahrenheit: ";
    cin >> TempFer;
    TempCel = Convert(TempFer);
    cout << "\nHeres the temperate in Celsius: " << TempCel << endl;
    return 0;
}
float Convert(float TempFer)
{
    float TempCel;
    TempCel = ((TempFer -32) * 5 ) / 9;
    return TempCel;
}