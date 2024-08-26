/* Demonstrate use of prefix and postix increment
and decrement operators */
#include <iostream>

int main()
{
    using namespace std;

    int myAge = 39;     // Initialize two Integers
    int yourAge = 75;
    
    cout << "I am: " << myAge << " years old.\n";
    cout <<  "You are: " << yourAge << " years old\n";
    myAge++;        // Postfix increment
    ++yourAge;      // prefix increment
    
    cout << "One year passes...\n";
    
    cout << "I am: " << myAge << " years old.\n";
    cout <<  "You are: " << yourAge << " years old\n";
    myAge++;        // Postfix increment
    ++yourAge;      // prefix increment

    cout << "Another year passes...\n";

    cout << "I am: " << myAge << " years old.\n";
    cout <<  "You are: " << yourAge << " years old\n";

    cout << "Let's print it again.\n";
    cout << "I am: " << myAge << " years old.\n";
    cout <<  "You are: " << yourAge << " years old\n";
    return 0;

}