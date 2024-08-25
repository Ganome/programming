// Demonstrate some math using a function
#include <iostream>
int Add( int first, int second)
{
    std::cout << "In Add() function, recived " << first << " and " << second << "\n";
    return(first + second);
}

int main()
{
    using namespace std;

    cout << "I'm in the main() function!\n";
    int a, b, c; // Declare some variables adding
    cout << "Enter two numbers: ";
    cin >> a;
    cin >> b;
    cout << "\nCalling Add() Function from main()\n";
    c=Add(a,b);
    cout << "\nBack in Main()\n";
    cout << "c was set to:\t" << c;
    cout << "\nExiting...\n\n";
    return 0;
}