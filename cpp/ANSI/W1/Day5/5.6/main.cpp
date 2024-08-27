/* Demonstrates multiple return statements */
#include <iostream>

using namespace std;

int Doubler(int AmountToDouble);

int main()
{
    int result = 0, input;

    cout << "Enter a number between 0 and 10,000 to double: ";
    cin >> input;

    cout << "\nBefore doubler is called...";
    cout << "\nInput #: " << input << " doubled: " << result << "\n";

    result = Doubler(input);

    cout << "\nBack from doubler()...\n";
    cout << "\ninput #: " << input << " doubled: " << result << endl;

    return 0;
}

int Doubler(int original)
{
    if (original <= 10000)
        return original * 2;
    else
        return -1;
    cout << "You cant get here!\n";
}