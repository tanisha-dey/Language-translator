#include <stdio.h>
#include <stdlib.h>

int main() {
    char command[1000];

    // Assuming python is in PATH, adjust the path if necessary
    sprintf(command, "python3 translator.py \"Hello, world!\" english spanish");

    // Execute the Python script
    system(command);

    return 0;
}
