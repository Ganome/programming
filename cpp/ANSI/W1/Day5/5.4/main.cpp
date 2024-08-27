/* Demonstrates passing by value.  This means that when you pass
a variable or value to a function; that function makes it's own
copy of the variable.  leaving the original value in tact in the calling function */
#include <iostream>
using namespace std;
void swap(int x, int y);

int main()
{
    int x = 5, y = 10;

    cout << "Main. Before swap, X: " << x << " Y: " << y << endl;
    swap(x,y);
    cout << "Main. After swap, X: " << x << " Y: " << y << endl;
}

void swap (int x, int y)
{
    int temp;

    cout << "in Swap. Before swap, X: " << x << " Y: " << y << endl;

    temp = x;
    x = y;
    y = temp;

    cout << "in Swap. After swap, X: " << x << " Y: " << y << endl;
}