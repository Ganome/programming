// Demonstrates the conditional operator "?"
#include <iostream>

int main()
{
    using namespace std;

    int x, y, z;
    cout << "Enter two numbers.\n";
    cout << "First number: ";
    cin >> x;
    cout << "\nSecond number: ";
    cin >> y;
    cout << endl;

    if (x > y)
        z = x;
    else
        z = y;
    
    cout << "After it test, z: " << z << endl;
    
    /* This line is read as “If expression1 (x>y) is true, return the value of expression2; otherwise,
return the value of expression3.” Assigned to variable "z" */
    z = (x > y) ? x : y;

    cout << "After conditional test, z: " << z << endl;
    return 0;
}