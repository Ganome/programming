// Demonstration on what a typedef is how to declare one.
#include <iostream>

typedef unsigned short int USHORT;

int main()
{
    using namespace std;
    USHORT Width = 5, Length;
    Length = 10;

    // create an unsigned short and initialize with results
    // of multiplying length by width
    unsigned short int Area = (Width * Length);

    cout << "Width:\t" << Width << endl;
    cout << "Length:\t" << Length << endl;
    cout << "Area:\t" << Area << endl;

    return 0;
}