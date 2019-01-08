#include <iostream>
using namespace std;
void ChangeData(int &a){
    a = 10;
}
int main(){
    int a = 5;
    int *b = &a;
    int &c = a;
    ChangeData(a);
    cout<<a<<' '<<b<<' '<<c<<endl;  //10 << 0x7ffee93e876c << 10
}
