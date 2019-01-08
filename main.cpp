#include <iostream>
using namespace std;
void ChangeData(int &a){
    a = 10;
}
void ChangePointer(int *a){
    *a = 15;
}
int* getPtr(){
    int a = 9;
    return &a;
}
int main(){
    int a = 5;
    int *b = &a;
    int &c = a;
    ChangeData(a);
    ChangePointer(b);
    cout << a << ' ' << b << ' ' << c << endl;  //15 0x7ffeec9a176c 15
    int* d = getPtr();
    cout << d << ' ' << *d << endl;             // является ошибкой но программа запускается, кадый раз выдавая разные адреса
}
