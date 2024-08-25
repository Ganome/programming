// Listing 2.4 - using the namespace std
#include <iostream>
int main()
{
    using namespace std;

    cout << "Hello there.\n";
    cout << "Here is 5:\t" << 5 << "\n";
    cout << "The manipulator endl ";
    cout << "writes a new line to the screen.";
    cout << endl;
    cout << "Here is a very big number:\t" << 70000000;
    cout << endl;
    cout << "Here is the sum of 8 and 5:\t";
    cout << 8+5 << endl;
    cout << "Here's a fraction:\t\t";
    cout << 5/8 << endl;
    cout << "And a very big number:\t\t";
    cout << 7000 * 6000 << endl;
    cout << "Dont forget to replace Jesse Liberty ";
    cout << "with your name...\n";
    cout << "Ganome is a C++ programmer!\n";
    return 0;
}