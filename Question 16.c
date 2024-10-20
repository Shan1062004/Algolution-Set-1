#include <stdio.h>

void printPattern(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= rows; j++) {
            if (j <= i) {
                printf("%d", j);
            } else {
                printf("%d", i);
            }
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printPattern(rows);
    return 0;
}
