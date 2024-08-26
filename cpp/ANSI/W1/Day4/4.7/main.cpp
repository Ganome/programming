/* Demonstrates why braces are important inside
nested if statements.  This program will exit early.
Not at the intended else clause, but in the nested if.*/
#include <iostream>

int main()
{
    using namespace std;

    int x; 
    cout << "Enter a number less than 10 or greater than 100: ";
    cin >> x;
    cout << "\n";

    if (x >= 10)
        if (x > 100)
            cout << "More than 100, Thanks!\n";
    else
        cout << "Less than 10, Thanks\n";

    return 0;
}