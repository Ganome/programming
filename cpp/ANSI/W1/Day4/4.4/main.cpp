/* Demonstrate use of if statement
used with relational operators */

#include <iostream>

int main()
{
    using namespace std;

    int metsScore, yankeesScore;
    cout << "Enter the score for the Mets: ";
    cin >> metsScore;

    cout<< "\nEnter the score of the Yankees: ";
    cin >> yankeesScore;

    cout << endl;

    if (metsScore > yankeesScore)
        cout << "Let's Go Mets!\n";

    if (metsScore < yankeesScore)
    {
        cout << "Go Yankees!\n";
    }
    if (metsScore == yankeesScore)
    {
        cout << "A tie? Naah, Can't be.\n";
        cout << "Give me the real score for the Yanks: ";
        cin >> yankeesScore;

        if (metsScore > yankeesScore)
            cout << "Knew it! Let's go Mets!\n";
        if (metsScore > yankeesScore)
            cout << "Wow, go Yanks!\n";
        if (metsScore == yankeesScore)
           cout << "Wow, it really was a tie!\n";
    }
    cout << "\n Thanks for telling me.\n";
    return 0;
}