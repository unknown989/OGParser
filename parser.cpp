#include <stdio.h>
#include "Parser.h"
//#include "String.h"

//using namespace std;

int main(){
	char* code = "print('hi');";
	Parser(code);
	return 0;
}

auto Parser(string code){
	printf(code);

}
