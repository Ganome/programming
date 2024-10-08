/* Demonstrates the use
default parameter values */

#include <iostream>

using namespace std;

int AreaCube(int length, int width = 25, int height = 1);

int main()
{
    int length = 100;
    int width = 50;
    int height = 2;
    int area;

    area = AreaCube(length, width, height);
    cout << "First area equals: " << area << endl;

    area = AreaCube(length, width);
    cout << "Second time area equals: " << area << endl;

    area = AreaCube(length);
    cout << "Third time area quals: " << area << endl;
    return 0;
}

int AreaCube(int length, int width, int height)
{
    return (length * width * height);
}