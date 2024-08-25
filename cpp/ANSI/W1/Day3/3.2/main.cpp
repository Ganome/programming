// Demonstration on how to use variables
#include <iostream>

int main()
{
    using namespace std;
    unsigned short int Width = 5, Length;
    Length = 10;

    // create an unsigned short and initialize with results
    // of multiplying length by width
    unsigned short int Area = (Width * Length);

    cout << "Width:\t" << Width << endl;
    cout << "Length:\t" << Length << endl;
    cout << "Area:\t" << Area << endl;

    return 0;
}