#include <iostream>
using namespace std;
int main(){
    int a = 5;      //5
    int *b = &a;    //0x7ffee082076c
    int &c = a;     //5
    cout<<a<<' '<<b<<' '<<c<<endl;
}