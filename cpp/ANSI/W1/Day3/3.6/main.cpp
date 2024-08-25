// Demonstrate printing characters based on numbers
#include <iostream>

int main()
{
    for (int i = 0; i<128; i++)
        std::cout << "i is equal to:\t" << i << "---: " << (char) i << std::endl;
    return 0;
}