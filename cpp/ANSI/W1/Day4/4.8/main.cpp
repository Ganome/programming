/* Demonstrates the proper way to use braces
to seperate if statements in advanced nested
if statements*/
#include <iostream>

int main ()
{
    using namespace std;

    int x;
    cout << "Enter a number less than 10 or greater than 100: ";
    cin >> x;
    cout << endl;

    if (x >= 100)
        {
            if (x > 100)
            cout << "More than 100, Thanks!\n";
        }
    else
        cout << "Less than 10, Thanks!\n";
    return 0;
}