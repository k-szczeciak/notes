my example usjing assertions:
```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef enum {
    false = 0,
    true
}bool;
  
  
void swap(int *a, int *b);
void printKS(int *a);
void test();
bool test_swap();
  
int main(){
  
int a = 10;
int b = -5;
    printf("a: %d, b: %d\n", a, b);
    swap(&a, &b);
    printf("a: %d, b: %d\n", a, b);
  
// int aa = 10;
// int *bb = NULL;
//     printKS(&aa);
//     printKS(bb);
  
  
    test();
  
return 0;
}
  
void swap(int *a, int *b){
    int c = *a;
    *a = *b;
    *b = c;
}
  

void printKS(int *a){

    assert(a != NULL);

    printf("value: %d\n", *a);

}

  

//// unit tests

void test(){

    int cnt= 0;

    assert(test_swap(5, -5));

    printf("test %d ok\n", ++cnt);

    assert(test_swap(5, 0));

    printf("test %d ok\n", ++cnt);

}

  
  

bool test_swap(int a, int b){

    int a_old = a;

    int b_old = b;

    swap(&a, &b);

    if ((a == a_old) && (b == b_old))

        return false;

    else

        return true;  

}
```


headder file:
``