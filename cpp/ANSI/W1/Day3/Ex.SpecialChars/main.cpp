// List of special chars that can be used in chat with cout
#include <iostream>

using namespace std;

int main()
{
    cout << "the \\a character is an ALERT (bell)" << endl;
    cout << "The \\b character is a backspace..\b" << endl;
    cout << "the \\f operater is for form feed \fTest after the flag" << endl;
    cout << "the \\n operator is a newline character.\n";
    cout << "\rthe \\r operator is a Carraige return.\n\r";
    cout << "the \\t operator is a \tTab" << endl;
    cout << "the \\v operator is a vertial \vtab\n";
    cout << "the \\' operator is a single quote character \'Quotation\'\n";
    cout << "the \\\" operator is for double \"quotes\"\n";
    cout << "the \? operator is for Question Mark\n";
    cout << "the \\ operator is for Backslash\n";
    cout << "the \\000 operator is for Octal Notation \101\101\n";
    cout << "the \\xhhh is for Hexadecimal Notation \xFF\xAA\n";
    return 0;
}