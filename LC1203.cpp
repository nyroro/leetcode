#include <unistd.h>
class Foo {
public:
    int n;
    Foo() {
        n=1;
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        while(n!=1)
        {
            usleep(1);
        }
        printFirst();
        n=2;
    }

    void second(function<void()> printSecond) {
        
        // printSecond() outputs "second". Do not change or remove this line.
        while(n!=2)
        {
            usleep(1);
        }
        printSecond();
        n=3;
    }

    void third(function<void()> printThird) {
        
        // printThird() outputs "third". Do not change or remove this line.
        while(n!=3)
        {
            usleep(1);
            
        }
        printThird();
        n=1;
        
    }
};