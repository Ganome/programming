/* Demonstrates function polymorphism
also known as function overloading */
#include <iostream>

using namespace std;

int Double(int);
long Double(long);
float Double(float);
double Double(double);

int main()
{
    int myInt = 6500;
    long myLong = 65000;
    float myFloat = 6.5F;
    double myDouble = 6.5e20;

    int doubledInt;
    long doubledLong;
    float doubledFloat;
    double doubledDouble;

    cout << "myInt: " << myInt << endl << "myLong: " << myLong << endl;
    cout << "myFloat: " << myFloat << endl << "myDouble: " << myDouble << endl;

    doubledInt = Double(myInt);
    doubledLong = Double(myLong);
    doubledFloat = Double(myFloat);
    doubledDouble = Double(myDouble);

    cout << "doubledInt: " << doubledInt << "\ndoubledLong: " << doubledLong << endl;
    cout << "doubledFloat: " << doubledFloat << "\ndoubledDouble: " << doubledDouble << endl;

    return 0;
}

int Double(int original)
{
    cout << "In Double*int)\n";
    return 2 * original;
}

long Double(long original)
{
    cout << "In Double(long)\n";
    return 2 * original;
}

float Double(float original)
{
    cout << "in Double(float)\n";
    return 2 * original;
}

double Double(double original)
{
    cout << "in Double(double)\n";
    return 2 * original;
}