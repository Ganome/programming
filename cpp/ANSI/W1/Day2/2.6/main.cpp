// Demonstrating a call to a function
#include <iostream>

/* function Demonstration Function
prints out a useful message */
void DemonstrationFunction()
{
    std::cout << "In Demo Function\n";
}

/* function main - prints out a message, then
calls DemonstrationFunction(), then prints out
a second message*/
int main()
{
    std::cout << "In main\n";
    DemonstrationFunction();
    std::cout << "Back in Main\n";
    return 0;
}