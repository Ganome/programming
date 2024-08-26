// Demonstrates advanced If statements
#include <iostream>

int main()
{
    /*Ask for two numbers
    Assign the numbers to bigNumber and littleNumber
    if bigNumber is bigger than littleNumber,
    see if they are evenly divisle
    If they are, see if they are the same number */

    using namespace std;

    int firstNumber, secondNumber;

    cout << "Enter two number.\nFirst: ";
    cin >> firstNumber;
    cout << "\nSecond: ";
    cin >> secondNumber;

    if ( firstNumber >= secondNumber)
    {
    if ( (firstNumber % secondNumber) == 0) //evenly divisble - no remainder
        {
            if (firstNumber == secondNumber)
                cout << "They are the same!\n";
        }
            else
                cout << "They are not evenly divisble!\n";
            return 0;
    }
}