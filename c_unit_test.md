gtest
catch2


all in folder: `C:\Windows\System32\cmd.exe` on my work computer
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
```c
//

// assert.h

//

//      Copyright (c) Microsoft Corporation. All rights reserved.

//

// Defines the assert macro and related functionality.

//

#if defined _VCRT_BUILD && !defined _ASSERT_OK

    #error assert.h not for CRT internal use

#endif

  

#include <corecrt.h>

  

#pragma warning(push)

#pragma warning(disable: _UCRT_DISABLED_WARNINGS)

_UCRT_DISABLE_CLANG_WARNINGS

  

_CRT_BEGIN_C_HEADER

  
  
  

#undef assert

  

#ifdef NDEBUG

  

    #define assert(expression) ((void)0)

  

#else

  

    _ACRTIMP void __cdecl _wassert(

        _In_z_ wchar_t const* _Message,

        _In_z_ wchar_t const* _File,

        _In_   unsigned       _Line

        );

  

    #define assert(expression) (void)(                                                       \

            (!!(expression)) ||                                                              \

            (_wassert(_CRT_WIDE(#expression), _CRT_WIDE(__FILE__), (unsigned)(__LINE__)), 0) \

        )

  

#endif

  
  
  

_CRT_END_C_HEADER

_UCRT_RESTORE_CLANG_WARNINGS

#pragma warning(pop) // _UCRT_DISABLED_WARNINGS
```