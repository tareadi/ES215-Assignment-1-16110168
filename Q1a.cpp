#include <iostream>
#include <stdint.h>  
#include <inttypes.h>
#include <stdio.h>   
#include <stdlib.h>

using namespace std;
int fib(unsigned __int64 x) {
   if((x==1)||(x==0)) {
      return(x);
   }else {
      return(fib(x-1)+fib(x-2));
   }
}
int main() {
   unsigned __int64 x = 100 , i=0;
   cout << "\nFib Series : ";
   while(i < x) {
      cout << " " << fib(i);
      i++;
   }
   return 0;
}
