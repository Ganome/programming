/* Demonstrates fibonacci series 
using recursion */
#include <iostream>
double fib(double n);

using namespace std;

int main()
{
    double n, answer;
    cout << "Enter number to find: ";
    cin >> n;
    cout << "\n\n";

    answer = fib(n);

    cout << answer << " is the " << n << "th Fibonacci number\n";
    return 0;
}

double fib(double n)
{
    cout << "Processing fib(" << n << ")...";
    
    if (n < 3)
    {
        cout << "Return 1!\n";
        return (1);
    }
    else
    {
        cout << "Call fib(" << n-2 << ") ";
        cout << "and fib (" << n-1 << ").\n";
        return (fib(n-2) + fib(n-1));
    }
}