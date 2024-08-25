#include <iostream>

int main()
{
    int x = 5;
    int y = 7;
    std::cout << std::endl;
    std::cout << x + y << " " << x * y << std::endl; // Added the std::endl on this line because the line below no longer exists in the standard
//    std::cout << std::end; //This no longer exists in the current C++ standard
    return 0;
}