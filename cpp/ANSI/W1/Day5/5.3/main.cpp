/* Demonstrates how the same variable name can be used in
 different functions with different values*/
 #include <iostream>
using namespace std; // Global Declaration

 void myFunc();

 int main()
 {
    using namespace std; // Local declaration

    int x = 5;
    
    cout << "In main the x value is: " << x << endl;

    myFunc();
    cout << "\nBack in main again - and X is: " << x << endl;
    return 0;
 }

 void myFunc()
 {
    int x = 8;
    cout << "In myFunc x is : " << x << endl;

    {
        cout << "\nIn a nested code block inside myFunc X is: " << x << endl;

        int x = 420;

        cout << "Very local inside codeblock defined X is: " << x << endl;
    }
    
    cout << "\nOut of the code block and back in myFun the x equals: " << x << " again.\n";
 }