// Demonstrate enumerated constants
#include <iostream>

using namespace std;

int main()
{
    enum Days { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

    Days today;
    today = Sunday;

    if (today == Sunday || today == Saturday)
        cout << "\nGotta love the weekends!\n";
    else
        cout << "\nBack to work.\n";

    return 0;
}