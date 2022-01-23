#include <iostream>
#include <stdint.h>  
#include <inttypes.h>
#include <stdio.h>   
#include <stdlib.h>

using namespace std;

int main(){
	unsigned __int64 n = 100;;
	unsigned __int64 f = 0, s = 1, t;
	for (int i = 0;i<n;i++){
		if(i==0){
			cout <<f<<" "<<s<<" ";
		}
		else{
			t = f + s;
			f = s;
			s = t;
			cout <<t<<" ";			
		}
	}
}
