/* Demonstrates the use of the else clause
while using the if condition */

#include <iostream>

int main()
{
    using namespace std;

    int firstNumber, secondNumber;
    cout << "Please enter a big number: ";
    cin >> firstNumber;
    cout << "\nPlease enter a smaller number: ";
    cin >> secondNumber;
    if (firstNumber > secondNumber)
        cout << "\nThanks!\n";
    else
        cout << "\nWow, you should go back to first grade.\n";

    return 0;
}