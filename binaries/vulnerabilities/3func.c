#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void HelloWorld() {
    printf("Hello, World!\n");
}


void firstCall(uint32_t num) {
    // *num = *num * 2;

    if (num > 50 && num <100)
         HelloWorld();
}

int main(int argc, char *argv[]) {


    // Convert command-line argument to integer
    // int number = atoi(argv[1]);

    uint32_t number = 60;

    firstCall(number);
    return 0;
}

