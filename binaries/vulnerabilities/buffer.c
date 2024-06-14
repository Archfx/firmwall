#include <stdio.h>
#include <string.h>

void secret_function() {
    printf("Unauthorized access to secret function!\n");
}

void vulnerable_function(char *input) {
    char buffer[10];
    strcpy(buffer, input);
    printf("Buffer contains: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
	printf("hello world");
    vulnerable_function(argv[1]);
    return 0;
}
