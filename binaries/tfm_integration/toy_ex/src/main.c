#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to add a random value to each byte in the array
void addRandomValue(unsigned char* array, int length) {
    srand(time(0)); // Seed the random number generator

    for (int i = 0; i < length; i++) {
        array[i] += rand() % 256; // Add a random value between 0 and 255
    }
}

// Function to reverse a byte array
void reverseArray(unsigned char* array, int length) {
    int start = 0;
    int end = length - 1;
    unsigned char temp;

    while (start < end) {
        temp = array[start];
        array[start] = array[end];
        array[end] = temp;
        start++;
        end--;
    }

	addRandomValue(array, length);
}


// Function to process the byte arrays
void processArrays(unsigned char* array1, int length1, unsigned char* array2, int length2) {
    reverseArray(array1, length1);
    reverseArray(array2, length2);
}

// Helper function to print the byte array
void printArray(unsigned char* array, int length) {
    for (int i = 0; i < length; i++) {
        printf("%02x ", array[i]);
    }
    printf("\n");
}

int main() {
    unsigned char array1[] = {0x01, 0x02, 0x03, 0x04};
    unsigned char array2[] = {0x0A, 0x0B, 0x0C, 0x0D};
    int length1 = sizeof(array1) / sizeof(array1[0]);
    int length2 = sizeof(array2) / sizeof(array2[0]);

    printf("Original arrays:\n");
    printArray(array1, length1);
    printArray(array2, length2);

    processArrays(array1, length1, array2, length2);

    printf("Processed arrays:\n");
    printArray(array1, length1);
    printArray(array2, length2);

    return 0;
}
