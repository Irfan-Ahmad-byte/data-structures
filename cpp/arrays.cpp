#include <iostream>

using namespace std;
#include <string>

int main() {
    int arr[4];

    for (int i = 0; i < sizeof(arr)/sizeof(int); i++)
    {
        arr[i]=i*2;
        cout << arr[i] << "\n";
    }
    cout << "array length " << sizeof(arr)/sizeof(int) << "\n";
    cout << "array size " << sizeof(arr) << "\n";
    // try to add an extra element to the above array
    string exception1;
    arr[7] = 12;

    // now try to create an array without pre defined length but some elements, and add some lements to it
    cout << "now try to create an array without pre defined length but some elements, and add some lements to it" << '\n';
    int arr2[] = {1,2,3,4,5};
    cout << "array 2 length " << sizeof(arr2)/sizeof(int) << "\n";
    cout << "array 2 size " << sizeof(arr2) << "\n";
    arr2[2] = 70;
    arr2[7] = 100;

    cout << "array 2 length after addition " << sizeof(arr2)/sizeof(int) << "\n";
    cout << "array 2 size after addition " << sizeof(arr2) << "\n";
    
    return 0;
}